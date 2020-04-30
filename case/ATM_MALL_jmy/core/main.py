#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/29 1:07
# @File: main.py
# @Software: PyCharm
import os,sys

# BASE_DIR=os.path.abspath(__file__)
# print((BASE_DIR))
# BASE_DIR=os.path.dirname(os.path.abspath(__file__))
# print((BASE_DIR))
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print((BASE_DIR))
sys.path.append(BASE_DIR)

from bin import bank,mall,seller





def choice_system():
    print("欢迎您！")
    ipt_choice_system=input("1.商城\n2.ATM\n3.卖家系统\n请选择您要登录的系统：")
    main_login(ipt_choice_system)




def login(func):
    def wrapper(*args,**kwargs):
        func(*args)
        switch_system=True
        system_type=args[0]
        while switch_system:
            if system_type=="1":
                username=input("请输入用户名：")
                password=input("请输入密码：")
                mall.mall_login(username,password)
            elif switch_system=="2":
                bank.bank_loggin(username,password)
            elif switch_system == "3":
                seller.seller_loggin(username, password)
            else:
                print("您的输入有误，请重新输入！")
                switch_system=False
                choice_system()
    return  wrapper
@login
def main_login(type):
    print("您选择的系统为：",type)

choice_system()

