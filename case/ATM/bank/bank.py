#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/27 15:22
# @File: shopping_mall.py
# @Software: PyCharm
import os


switch_bank=True  #银行程序总开关
switch_cus_choisc=True  #用户输入指令开关
str_username="请输入用户名："
str_password="请输入密码："
str_wrong_msg="您的输入有误，请重新输入！"
str_not_exist="您输入的用户不存在"
limit=0

#登录方法 return=1时登录成功，return=0时输入信息有误
def login_bank(username,password):
    with open("cus_info_bank.txt","r",encoding="utf-8") as f_userinfo:
        for line in f_userinfo:
            _line=line.strip().split(",")
            if username==_line[0] and password==_line[1]:
                print("%s,登陆成功！"%username)
                return 1,_line[2]
            else:
                print(str_wrong_msg)
                return 0
        print(str_not_exist)
        return 2

#提现方法
def cash_out(cash_out_limit):
    with open("cus_info_bank.txt","r",encoding="utf-8") as f_userinfo:
        with open("cus_info_bank.dat","w",encoding="utf-8") as new_file:
            for line in f_userinfo:
                _line=line.strip().split(",")
                cash_out_limit=int(_line[2])/2
                if int(user_cash_out)<=cash_out_limit:
                    cash_out_limit=cash_out_limit-int(user_cash_out)
                    print("您已成功提现：", int(user_cash_out), "您的现金额度为：", int(cash_out_limit))
                    _line[2]=int(_line[2])/2+cash_out_limit
                    line=_line[0]+","+_line[1]+","+_line[2]+","+_line[3]

                new_file.write(line)
                new_file.flush()
    os.replace("cus_info_bank.dat","cus_info_bank.txt")



while switch_bank:
    print("Welcome!")
    username = input(str_username)
    password = input(str_password)
    # 执行登录方法，登录成功返回结果1
    login_result=login_bank(username,password)
    if login_result[0]==1:
        limit = int(login_result[1])
        while switch_cus_choisc:
            cus_choisc_bank = input("1.查询额度\n2.提款\n3.还款\n4.转账\n5.查询账单\n6.退出\n请选择指令：")

            if cus_choisc_bank=="1":
                print("您的信用卡额度为：",limit)
            elif cus_choisc_bank=="2":
                cash_out_limit=limit/2
                print("您可提现的额度为：",int(cash_out_limit))
                user_cash_out=input("请输入您要提现的金额（手续费5%）：")
                cash_out(cash_out_limit)
            elif cus_choisc_bank == "3":
                pass
            elif cus_choisc_bank == "4":
                pass
            elif cus_choisc_bank == "5":
                pass
            elif cus_choisc_bank == "6":
                pass
            else:
                print(str_wrong_msg)




