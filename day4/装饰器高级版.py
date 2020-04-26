#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/24 23:20
# @File: 装饰器高级版.py
# @Software: PyCharm
user,passwd='alex',"abc"
def auth(auth_type):
    print("auth func:",auth_type)
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper func args:",*args,**kwargs)
            username = input("Username:").strip()
            password = input("Password:").strip()
            if user == username and passwd == password:
                print("登录成功！")
                return func(*args, **kwargs)
            else:
                exit("输入信息有误")
        return wrapper
    return out_wrapper

# def index():
#     print("welcome!")

@auth(auth_type="local")     # home=auth()
def home():
    print("welcome to home!")
    return "from home"
@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs!")
# index()
print(home())
bbs()
