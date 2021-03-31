import sys
import requests
import common.config
import json
import xlrd
import sys
import lib.method
from common.config import cf
from common.get_log import log

def methodpost(url, headers,data,timeout=30):

    res = requests.request("POST", url=eval(url), data=eval(data),headers=eval(headers),timeout=timeout)
    return res


def get_json(res):
    #获取返回json
    print('res.json：\n',res.json())
    return res.json()





url = 'https://onestopdata.pactera.com/chabeiapi/chabei/credit/doLogin'
headers = {
    'Content-Type':'application/x-www-form-urlencoded',
    'Accept':'application/json',
    'agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
          }

data = {
    "username": "ICBCadmin",
    "password": "icbc2019",
    "clientCode": "CHA_ICBC_ICBC_310100_001"
        }

lib.method.Tools().read_excel("用例数据","login_01")
print(lib.method.excel_dict["body"])

res = methodpost(url=cf.get_key("params","url"),headers=cf.get_key("params","headers"),data=lib.method.excel_dict["body"])
print(res.text)


# url = 'https://onestopdata.pactera.com/chabeiapi/chabei/credit/doLogin'
# headers = {
#     'Content-Type':'application/x-www-form-urlencoded',
#     'Accept':'application/json',
#     'agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
#           }
#
# data = {
#     "username": "ICBCadmin",
#     "password": "icbc2019",
#     "clientCode": "CHA_ICBC_ICBC_310100_001"
#         }
#
# res = requests.request("POST", url, params=data,headers=headers,timeout=30)
# print(res.text)