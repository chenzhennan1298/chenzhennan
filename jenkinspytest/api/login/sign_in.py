from api.base_api import BaseApi



class Signin(BaseApi):

    api_path = "data\login\login.yml"
    def signin(self,username ,password):
        # Template模板二次修改的值，p_data
        p_data = {"ip":self.ip,"username":username,"password":password}
        # 获取响应，进行了多次封装
        res = self.send_api_data(self.api_path,p_data,sub=None)
        return res


