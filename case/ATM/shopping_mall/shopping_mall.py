#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/27 15:22
# @File: shopping_mall.py
# @Software: PyCharm


swich_mall =True
str_choice_system="1.商城\n2.银行\n请选择您要登录的系统："
str_username="请输入用户名："
str_password="请输入密码："
# login_suc=1  #登录成功
str_wrong_msg="您的输入有误，请重新输入！"
str_not_exist="您输入的用户不存在"



#登录方法 return=1时登录成功，return=0时输入信息有误
def login_mall():
    with open("cus_info_mall.txt","r",encoding="utf-8") as f_userinfo:
        for line in f_userinfo:
            _line=line.strip().split(",")
            if username==_line[0] and password==_line[1]:
                login_suc=1
                print("%s,登陆成功！"%username)
                return 1,_line[2]
            else:
                print(str_wrong_msg)
                return 0
        print(str_not_exist)
        return 2

#展示商品信息方法
def show_item():
    with open("item_list.txt","r",encoding="utf-8") as f_item_list:
        count=0
        for line in f_item_list:
            count+=1
            _line =line.strip().split(",")
            print(count,_line[0],_line[1])
        return count

while swich_mall:
    print("welcome!")
    choice_system=input(str_choice_system)
    if choice_system=="1":
        username=input(str_username)
        password=input(str_password)
        #执行登录方法
        login_mall()
        #执行展示商品信息方法
        show_item()
        buy_item=input("请选择您要购买的商品序号:")



    elif choice_system=="2":
        pass
    else:
        print(str_wrong_msg)

