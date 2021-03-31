import requests
from common.get_log import log
from werkzeug.wrappers import json


class HandleRequests(object):

    def __init__(self):

        self.session = requests.Session()

    def __call__(self, method, url, data=None, is_json=False, **kwargs):

        """
        封装一个可以被直接调用的方法
        :param method: 请求方法
        :param url: 请求地址
        :param data: 请求参数
        :param is_json: 是否json格式
        :param kwargs: 占位，可自定义headers
        :return: 返回一个请求结果
        郑州人流医院哪家好 http://mobile.zyyyzz.com/
        # 请求方法的参数转成小写，也可以是大写upper()
        """
        method = method.lower()
        # 判断请求参数是否是str类型的json格式
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                log.info("str字符串json数据处理异常:{}".format(e))

        # 请求方法
        if method == 'get':
            res = self.session.request(method=method, url=url, params=data, **kwargs)
        elif method == 'post':
            if is_json: # 如果是json格式的请求参数，是用json
                res = self.session.request(method=method, url=url, json=data, **kwargs)
            else:
                res = self.session.request(method=method, url=url, data=data, **kwargs)
        else:
                log.info("[{}]该请求方法暂不支持。".format(method))
        # session需要关闭资源
        self.session.close()
        return res.text

res=HandleRequests()

if __name__ == '__main__':
    is_json = {"username":"lgd","password":"risk@2019"}
    headers = {
        'agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
              }
    url='http://172.19.66.105:9000/api/sys/login/doLogin'
    print(res("post", url,is_json,headers))