from api.base_api import BaseApi

class Individualclients(BaseApi):

    def __init__(self):
        self.api_path = "data\individualclients\individualclients.yml"
    #新增个人客户
    def add_individual_clients(self,certType,certId,customerName,country,customerId,surName,name,customerType):

        p_data = {"ip":self.ip,"certType":certType,"certId":certId,"customerName":customerName,"country":country,"customerId":customerId,"surName":surName,"name":name,"customerType":customerType}

        res = self.send_api_data(self.api_path,p_data,"add")
        return res

    #删除个人客户
    def delete_individual_clients(self,id):

        p_data = {"ip":self.ip,"id":id}

        res = self.send_api_data(self.api_path,p_data,"delete")
        return res
