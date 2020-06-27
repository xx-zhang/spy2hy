# coding:utf-8

import os
# AUXI_DIR = os.path.abspath(os.path.abspath(os.path.abspath(__file__)))
DEFAULT_HEADER_FILE_PATH = 'D://WorkSpace//spy4hy//auxi//data//req_header.txt'
DUMP_DATA_DIR = os.path.join('D://results//')

WIN_LOG_DIR = 'd://results//logs//'
LINUX_LOG_DIR = '/data/spyder4hy/logs/'

# TODO 这里是使用 firefox工具导出的，本人很推荐这种弄法，在低版本的requests上可以避免很多问题。
firefox_request = {
          "bodySize": 42,
          "method": "POST",
          "url": "https://sc.122.gov.cn/m/viopub/getVioPubList",
          "httpVersion": "",
          "headers": [
            {
              "name": "Host",
              "value": "sc.122.gov.cn"
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
              "name": "Content-Type",
              "value": "application/x-www-form-urlencoded; charset=UTF-8"
            },
            {
              "name": "X-Requested-With",
              "value": "XMLHttpRequest"
            },
            {
              "name": "Content-Length",
              "value": "42"
            },
            {
              "name": "Origin",
              "value": "https://sc.122.gov.cn"
            },
            {
              "name": "Connection",
              "value": "keep-alive"
            },
            {
              "name": "Referer",
              "value": "https://sc.122.gov.cn/"
            },
            {
              "name": "Cookie",
              "value": "_uab_collina=159322436487323186661115; JSESSIONID-L=95ddef00-e4fc-4c37-b8c6-f6f9c191bbbd"
            }
          ],
          "cookies": [
            {
              "name": "_uab_collina",
              "value": "159322436487323186661115"
            },
            {
              "name": "JSESSIONID-L",
              "value": "95ddef00-e4fc-4c37-b8c6-f6f9c191bbbd"
            }
          ],
          "queryString": [],
          "headersSize": 628,
          "postData": {
            "mimeType": "application/x-www-form-urlencoded",
            "params": [
              {
                "name": "page",
                "value": "5"
              },
              {
                "name": "size",
                "value": "20"
              },
              {
                "name": "startTime",
                "value": ""
              },
              {
                "name": "endTime",
                "value": ""
              },
              {
                "name": "gsyw",
                "value": "01"
              }
            ],
            "text": "page=5&size=20&startTime=&endTime=&gsyw=01"
          }
        }