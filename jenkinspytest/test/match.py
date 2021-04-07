# import re
#
# from math import factorial
#
#
# class Match():
#
#     def ysmatch(self):
#         line = "Cat1s are smarter23214 than dogs31,Cat1s are smarter23214 than dogs31"
#         lines = """{"globalId":"","appId":"","requestId":"","serviceId":"CustomerInfoSmartformApplicationService","requestType":"SMARTFORM","action":"add","parameters":{"entity":{"certType":"Ind01","certId":"21415115212","customerName":"testin","country":"中国","customerId":"2145112515","status":"1","surName":"陈","name":"卫国","customerType":"01"}}}"""
#         b = "testing"
#         # a = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
#         # a = re.search(r'than',line,re.M|re.I)
#         # if a == None:
#         #     print("none")
#         # else:
#         #     print(a.group())
#         c = re.search(r'(.*)"certId":"(.*?)","(.*)',lines,re.M|re.I)
#         d = re.search(r'.*smarter(\d+).*',line,re.M|re.I)
#         e = re.search(r'.*smarter(\d+).*',line,re.M|re.I)
#         f = re.search("a","aa")
#         print(f.group())
#         # print(a.group())
#
#     def mhh(self,n):
#         if n==1:
#             return n
#         n = n*self.mhh(n-1)
#         return n
# # Match().ysmatch()
# print(Match().mhh(4))




