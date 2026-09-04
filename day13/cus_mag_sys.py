import re


class Customer:
    """客户类"""
    def __init__(self, id, name, age, tel, email):
        self.id = id
        self.name = name
        self.age = age
        self.tel = tel
        self.email = email

class Cus_Sys:
    """客户管理系统类"""
    def __init__(self,customers=[]):
        self.__customers = customers

    def add_customer(self):
        count = 1
        pattern = r"^\d+$"
        while True:
            id = input("请输入客户id:")
            if re.match(pattern, id):
                break
            else:
                print("客户id必须为纯数字")
                count += 1
            if count == 3:
                print("最后一次机会，",end="")
            if count >3:
                return
        name = input("请输入客户name:")
        age = input("请输入客户age:")
        tel = input("请输入客户tel:")
        email = input("请输入客户email:")

if __name__  == "__main__":
    cs = Cus_Sys()
    cs.add_customer()