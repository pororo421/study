#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/28 22:37
# @File: seller.py
# @Software: PyCharm
def seller_login(account,password):
    print("卖家系统".center(50,"*"))
    print("欢迎您登录\n你的账户为%s：\n您的密码为：%s" %(account,password))
    if "登陆成功":
        opration_item()
        print("登录成功")
        '''
            1.添加
            2.修改
            3.删除
        '''

def opration_item():
    print("商品操作方法！")