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
try:
    from .logger import Log
    logging = Log(log_flag='spyder_running_status')
except:
    import logging

try:
    from .config import DUMP_DATA_DIR as dump_data_dir
except:
    # TODO 如果本地并没有存储的相关配置，那么默认指定这个。
    dump_data_dir = 'd://results//'


from .config import firefox_request
request_headers = {x['name']: x['value'] for x in firefox_request['headers']}
request_cookies = {x['name']: x['value'] for x in firefox_request['cookies']}


class ViopubSpyderApiManager():

    def __init__(self, city_short=None, vpid=None):
        self.city_short = city_short
        self.vpid = vpid

    @staticmethod
    def write_to_local(json_data, path):
        _txt = json_data
        if type(json_data) == dict:
            _txt = json.dumps(json_data)
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        with open(path, 'w+', encoding='utf-8') as f:
            f.write(_txt)
            f.close()

    @staticmethod
    def get_parse_header():
        from .request_tool import ParseReqHeader
        from .config import DEFAULT_HEADER_FILE_PATH
        return ParseReqHeader.parse1(file_path=DEFAULT_HEADER_FILE_PATH)

    @staticmethod
    def fetch_url(url, method='post', data=None,
                  headers=request_headers, cookies=request_cookies, **kwargs):
        response = request(method=method, url=url,
                           headers=headers, cookies=cookies,
                           data=data, timeout=10, )
        status_code = response.status_code
        logging.warn('Prepare to Patch URL: {}'.format(url))
        if status_code != 200:
            logging.error('Headers Error [{code}] for Server. \n{text}'.format(
                code=str(status_code), text=response.text))
            return None
        _res = json.loads(response.text)
        _status = _res.get('code')
        if _status != 200:
            logging.error('payload Error. {}'.format(response.text))
            return None
        return _res

    def get_list(self, page=2, save_local=True):
        _list_url = "https://{city_short}.122.gov.cn/m/viopub/getVioPubList".format(city_short=self.city_short)
        data = {"page": page, "size": 20, "startTime": "&", "endTime": "&", "gsyw": "01"}
        res_data = ViopubSpyderApiManager.fetch_url(url=_list_url, data=data)
        if not res_data:
            logging.error('REQUEST_DATA_ERROR: {}'.format(_list_url))
            return None
        if save_local:
            data_dump_dir = os.path.join(dump_data_dir, self.city_short, 'lists')
            _saved_path = os.path.join(data_dump_dir, 'list_page_{}.txt'.format(str(page)))
            ViopubSpyderApiManager.write_to_local(json_data=res_data, path=_saved_path)
        return res_data

    def get_detail(self, save_local=True):
        _detail_url = "https://{city_short}.122.gov.cn/m/viopub/getVioPubDetail".format(city_short=self.city_short)
        data = {'id': self.vpid}
        res_data = ViopubSpyderApiManager.fetch_url(url=_detail_url, data=data,
                                                    headers={"User-Agent": "Local Test"},
                                                    cookies=None)
        if not res_data:
            logging.error('REQUEST_DATA_ERROR: {}'.format(_detail_url))
            return None
        if save_local:
            data_dump_dir = os.path.join(dump_data_dir, self.city_short, 'details')
            _saved_path = os.path.join(data_dump_dir, '{}.txt'.format(str(self.vpid)))
            ViopubSpyderApiManager.write_to_local(json_data=res_data, path=_saved_path)
        return res_data


# if __name__ == '__main__':
#     logging.warning('---------------------')
#     # _test = ViopubSpyderApiManager(city_short='hb', vpid='42000210000000373477').get_detail()
#     _test = ViopubSpyderApiManager(city_short='hb', vpid='42000210000000373477').get_list()
#     logging.warning(_test)