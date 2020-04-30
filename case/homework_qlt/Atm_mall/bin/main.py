#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/28 22:41
# @File: main.py
# @Software: PyCharm

import os,sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

sys.path.append(BASE_DIR)

from core import bank,mall,seller

# def auth(system_type):
#     def login(func):
#         def wrapper(*args,**kwargs):
#             username = input("请输入用户名：")
#             password = input("请输入密码：")
#             if system_type == "1":
#                 bank.bank_login(username,password)
#             elif system_type == "2":
#                 mall.mall_login(username,password)
#             elif system_type == "3":
#                 seller.seller_login(username,password)
#             else:
#                 print("输入有误！请重新输入！")
#         return wrapper
#     return login


def login(func):
    def wrapper(*args,**kwargs):
        func(*args)
        username = input("请输入用户名：")
        password = input("请输入密码：")
        system_type = args[0]
        swich_system = True
        while swich_system:
            if system_type == "1":
                mall.mall_login(username, password)
            elif system_type == "2":
                bank.bank_login(username, password)
            elif system_type == "3":
                seller.seller_login(username,password)
            else:
                print("输入有误！请重新输入！")
                swich_system = False
                choice_system()
    return wrapper

@login
def mian_login(type):
    print("选择的系统是：",type)
    return "请重新输入！"


def choice_system():
    print("欢迎进入ATM系统")
    ipt_system_num = input("请选择要登录的系统：\n1.商城\n2.ATM\n3.卖家系统")
    mian_login(ipt_system_num)

choice_system()