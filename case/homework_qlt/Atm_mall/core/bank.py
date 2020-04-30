#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/28 22:37
# @File: bank.py
# @Software: PyCharm

def bank_login(account,password):
    print("银行系统".center(50,"*"))
    print("欢迎您登录\n你的账户为%s：\n您的密码为：%s" %(account,password))
    if "登录成功":
        opration_balance()


def opration_balance():
    print("1.转账\n2.提现")
