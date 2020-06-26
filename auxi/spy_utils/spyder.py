# coding:utf-8
"""
API 解读过程
1. 首先发现全国的URL列表存在位置在
    - https://static.122.gov.cn/V1.18.4/static/js/funcDistrict.js
2. 针对单个zf机构的列表查询，我们可以发现。这里有一个列表和时间的查询。
    - https://{city_short}.122.gov.cn/m/viopub/getVioPubList
    - NOTE: city_short 对应的就是之前的bj、tj等（省市的缩写）
3. 获取详情
    - NOTE: 针对每一个列表查看详情后, 可以得到一个详情介绍的Json（页面上渲染出的内容）
    - https://{city_short}.122.gov.cn/m/viopub/getVioPubDetail  POST
"""
import os
import json
from requests.api import request


from .config import DEFAULT_HEADER_FILE_PATH as dhfp, DUMP_DATA_DIR
from .request_tool import ParseReqHeader

default_cookies = {"insert_cookie":"67313298","TS011422ee":"015e99a05db939dccaf56cc4b90a501db4c6a366c045a2341988250ee63ae6cd61670266345ac93771b678106a44a4b09f2508d673","JSESSIONID-L":"980a5ee5-6b75-40d7-8ec3-1b3534262ee3","_uab_collina":"159317921486025403549109"}
default_headers = {
          "bodySize": 0,
          "method": "POST",
          "url": "https://bj.122.gov.cn/m/syscode/getFeedBackConfig",
          "httpVersion": "HTTP/1.1",
          "headers": [
            {
              "name": "Host",
              "value": "bj.122.gov.cn"
            },
            {
              "name": "User-Agent",
              "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"
            },
            {
              "name": "Accept",
              "value": "application/json, text/javascript, */*; q=0.01"
            },
            {
              "name": "Accept-Language",
              "value": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
            },
            {
              "name": "Accept-Encoding",
              "value": "gzip, deflate, br"
            },
            {
              "name": "X-Requested-With",
              "value": "XMLHttpRequest"
            },
            {
              "name": "Origin",
              "value": "https://bj.122.gov.cn"
            },
            {
              "name": "Connection",
              "value": "keep-alive"
            },
            {
              "name": "Referer",
              "value": "https://bj.122.gov.cn/"
            },
            {
              "name": "Cookie",
              "value": "insert_cookie=67313298; TS011422ee=015e99a05db2a64f901e7d789eefb02c76af76e06ed514988521a6811301f27f6912a7cf0d7060c5af4ad5cdc20f03f6e07d0131f0; JSESSIONID-L=980a5ee5-6b75-40d7-8ec3-1b3534262ee3; _uab_collina=159317921486025403549109"
            },
            {
              "name": "Content-Length",
              "value": "0"
            }
          ],
          "cookies": [
            {
              "name": "insert_cookie",
              "value": "67313298"
            },
            {
              "name": "TS011422ee",
              "value": "015e99a05db2a64f901e7d789eefb02c76af76e06ed514988521a6811301f27f6912a7cf0d7060c5af4ad5cdc20f03f6e07d0131f0"
            },
            {
              "name": "JSESSIONID-L",
              "value": "980a5ee5-6b75-40d7-8ec3-1b3534262ee3"
            },
            {
              "name": "_uab_collina",
              "value": "159317921486025403549109"
            }
          ],
          "queryString": [],
          "headersSize": 711
        }


def change_list_2dict(__list):
    _res = {}
    for x in __list:
        _res[x['name']] = x['value']
    return _res


class ViopubSpyderApiManager():

    def __init__(self, city_short=None, vpid=None):
        self.city_short = city_short
        self.vpid = vpid

    @staticmethod
    def fetch_url(method, url=None, data=None, files=None,
                  headers=None, proxies=None, json=None, cookies=None):
        if not headers:
            # headers = ViopubSpyderApiManager.get_header()
            headers = change_list_2dict(default_headers['headers'])
        if not cookies:
            cookies = change_list_2dict(default_headers['cookies'])
        print(headers)
        print(url) # https://bj.122.gov.cn/m/viopub/getVioPubDetail
        print(data)
        response = request(method=method, url=url,
                           data=data, files=files, json=json,
                           headers=headers, proxies=proxies, verify=False,
                           cookies=cookies)
        return response


    @staticmethod
    def get_header(dhfp=dhfp, header_txt=None):
        if header_txt:
            return ParseReqHeader().parse1(request_text=header_txt)
        return ParseReqHeader().parse1(file_path=dhfp)

    def get_detail(self):
        city_short = self.city_short
        id = self.vpid
        _detail_url = "https://{city_short}.122.gov.cn/m/viopub/getVioPubList".format(city_short=city_short)

        # 开始抓取后台接口的URL
        response = ViopubSpyderApiManager.fetch_url(method='post',
                                                    url=_detail_url,
                                                    data={'id': id},
                                                    )
        print(response.text)

        _res = json.loads(response.text)
        if int(_res['code']) == 200:
            print('获取成功')
        else:
            print('ERROR!')
            return False
        DUMP_FILE_DIR = os.path.join(DUMP_DATA_DIR, city_short)
        if os.path.exists(DUMP_FILE_DIR):
            os.makedirs(DUMP_FILE_DIR)
        with open(DUMP_FILE_DIR, str(id) + '.txt' ) as f:
            f.write(response.text)
            f.close()
        return True
