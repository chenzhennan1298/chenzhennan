import requests

class TestAssert():

    def test_assert(self):
        r = requests.get('http://www.baidu.com')
        assert r.status_code == 100, "返回200说明访问成功"



