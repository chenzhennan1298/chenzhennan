import pytest
import allure
from api.login.sign_in import Signin
from common.get_log import log


@allure.feature("signin")
class TestSignin():

    login = Signin()
    @classmethod
    def setup_class(cls):
        print('\n === 初始化-类 ===')


    @classmethod
    def teardown_class(cls):
        print('\n === 清除 - 类 ===')


    def test_login(self):
        log.info("--------开始测试")
        res = self.login.signin("lgd","risk@2019")
        log.info("--------结束测试")
        assert res["code"] == "200","当前值为%s"
