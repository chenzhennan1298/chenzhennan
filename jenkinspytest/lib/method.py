import sys
import requests
import common.config
import json
import xlrd
import sys
import re
from common.config import cf
from common.get_log import log


excel_dict = {}
res = None

class Request(object):
    request_dict = {}
    def __init__(self):
        self.__name__ = ""

    def methodget(self,url, headers,data,params,timeout=30):
        try:
            res = requests.request("GET", url,data=eval(data),params=params, headers=headers, timeout=timeout)
            status_code = re.findall("\d+",str(res))[0]
            log.logger.info('请求状态码：'+ status_code)
            return res

        except Exception:
            funcName = sys._getframe(0).f_code.co_name
            raise scriptError(funcName +"请求异常")
        except TypeError:
            log.logger.error('传入参数类型错误！')
        # finally:
        #     if res.status_code != 200: log.logger.error('请求返回状态不正常')


    # def methodrequest(self, methods,url, **kwargs):
    #     res = requests.request(methods,url,**kwargs)
    #     return res


    def methodpost(self,url, headers,data,timeout=30):

        try:

            res = requests.request("POST", url=eval(url), data=eval(data),headers=eval(headers),timeout=timeout)
            status_code = re.findall("\d+",str(res))[0]
            log.logger.info('请求状态码：'+ status_code)
            return res
        except Exception:
            funcName = sys._getframe(0).f_code.co_name
            raise scriptError(funcName +"请求异常")
        except TypeError:
            log.logger.error('传入参数类型错误！')
        # finally:
        #     if res.status_code != 200: log.logger.error('请求返回状态不正常'+ str(res.status_code))


    def get_code(self,res):
        # 获取返回状态码
        return res.status_code


    def get_json(self,res):
        #获取返回json
        # print(res)
        # if isinstance(res, str):
        #     try:
        #          json.loads(res, encoding='utf-8')
        #     except ValueError:
        #         return False
        # else:
        #     Logger().logger.error('返回不是json格式')
        #     return False
        try:
            print('res.json：\n',res.json())
            return res.json()
        except json.decoder.JSONDecodeError:
            log.logger.error('返回不是json格式')


    def get_text(self,res):
        #获取返回文本
        print('res.text：\n',res.text)
        return res.text


    def get_time(self,res):
        #获取响应执行时间,单位s
        time=res.elapsed.total_seconds()
        print('res.time：\n',res.elapsed.total_seconds())
        return time


    # def get_header(self,act):
    #     if act=="json":
    #
    #         json_header={
    #         'content-type': "application/json",
    #         }
    #         return json_header
    #     else:
    #         str_header={
    #             'content-type': "application/x-www-form-urlencoded",
    #         }
    #         return str_header

class Tools(object):


    def analysis_json(self,json_txt,key_name):

        if isinstance(json_txt,dict):

            if key_name in json_txt.keys():
                return json_txt[key_name]
        else:
            print('传入参数不是字典')

    def read_excel(self,sheetname,module): # module模块 column_name列名


        try:
            xlsfile = r"E:\python_work\jenkinspytest\test_ex.xlsx"# 打开指定路径中的xlsx文件
            book = xlrd.open_workbook(xlsfile)    #得到Excel文件的book对象，实例化对象
            for name in book.sheet_names():
                index = 0
                if sheetname == name:
                    index += 1
                    sheet_name = sheetname
                    break
                index += 1
            sheet0 = book.sheet_by_index(index)       # 通过sheet索引获得sheet对象
            # sheet_name = book.sheet_names()[0]    # 获得指定索引的sheet表名字
            sheet1 = book.sheet_by_name(sheet_name)    # 通过sheet名字来获取，当然如果知道sheet名字就可以直接指定
            nrows = sheet0.nrows     # 获取行总数
            ncols = sheet0.ncols     #获取列总数

            #获取指定模块指定列内容
            for i in range(nrows):
                if sheet1.row_values(i)[0] == module:
                    module_row = i
                    for excel_dict_key in sheet1.row_values(0):   #循环取excel作为字典的key且赋空值
                        excel_dict[excel_dict_key] = None

                    for j in excel_dict:
                        excel_dict[j] = sheet1.row_values(i)[sheet1.row_values(0).index(j)]
                    return excel_dict
        except Exception:
            funcName = sys._getframe(0).f_code.co_name
            raise scriptError(funcName +"获取excel值异常")


class business(object):

    def login(self,url,headers,data):
        qus = Request().methodpost(url=url,headers=headers,data=data)
        response_login = Request().get_json(qus)
        return response_login






class scriptError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

if __name__ == "__main__":



    Tools().read_excel("用例数据","login_01")

    a = business().login(url=cf.get_key("params","url"),headers=cf.get_key("params","headers"),data=excel_dict["body"])

    print(a)

