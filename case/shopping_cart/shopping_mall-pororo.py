# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/22 22:24
# @File: bank-pororo.py
# @Software: PyCharm
import getpass
import os

switch_mail = True  # 整个程序开关
switch_choice_product = True  # 买家购买商品开关
switch_product =True  #卖家商品列表开关
str_wrong_msg = "您的输入有误，请重新输入！"
str_username = "请输入用户名："
str_password = "请输入密码："
str_login_suc = "%s欢迎您!"
str_login_fal = "您输入的密码有误，请重新输入！"
str_login_not_exist = "您输入的用户不存在，请重新输入！"
str_choice_product = "请选择您要购买的商品："
balance = 0
str_product_order = '''
1.添加(命令：add,商品名称，价格)                       #例：add,samsung,999
2.删除(命令：del,商品序号)                            #例：del,1
3.修改(命令：edit,商品序号，新商品名称，新商品价格)     #例:edit,1,xiaomi,999
'''


# 买家登录方法 用户登录成功:return1,密码错误：return0,用户不存在：return2
def login_cus(username, password):
    with open("cus_info.txt", "r", encoding="utf-8") as f_cus_info:
        for line in f_cus_info:
            _line = line.strip().split(",")
            if username == _line[0]:
                if password == _line[1]:
                    print(str_login_suc % username)
                    return "1", _line[2]
                else:
                    print(str_login_fal)
                    return "0"
        print(str_login_not_exist)
        return "2"


# 展示商品信息方法
def product_list():
    with open("shoppingmall_list.txt", "r", encoding="utf-8") as f_product_list:
        count = 0
        for line in f_product_list:
            _line = line.strip().split(",")
            count += 1
            print(count, _line[0], _line[1])
        return count


# 更改购买商品清单
def modify_shopping_list(username, product, price):
    with open("shopping_list.txt", "r", encoding="utf-8") as f_product_list:
        with open("shopping_list.bak", "w", encoding="utf-8") as new_file:
            for line in f_product_list:
                list = line.split(":", 1)
                # print(_line)
                cus = list[0]
                if cus == username:
                    shopping_list = list[1].replace("[", "").replace('"', "").replace("]", "").replace("\n",
                                                                                                       "").replace(" ",
                                                                                                                   "").split(
                        ",")

                    shopping_list.append(product + ":" + price)

                    line = username + ":" + str(shopping_list).replace(" ", "") + "\n"
                    line = line.replace("'", '"')
                new_file.write(line)
                new_file.flush()
    os.replace("shopping_list.bak", "shopping_list.txt")


# 输出购买的商品信息
def bought_product(product, price):
    with open("shoppingmall_list.txt", "r", encoding="utf-8") as f_product_list:
        count = 0
        for line in f_product_list:
            _line = line.strip().split(",")
            count += 1
            if int(cus_choice) == count:
                print("您购买的商品为：", _line[0], _line[1])


# 修改余额
def modify_balance(username, balance):
    with open("cus_info.txt", "r", encoding="utf-8") as f_cus_info:
        with open("cus_info.dat", "w", encoding="utf-8") as f_new:
            for line in f_cus_info:
                _line = line.strip().split(",")
                if username in _line:
                    line = str(_line).replace(_line[2], str(balance))
                    print(line)
                    line = line.replace("[", "").replace("'", "").replace("]", "").replace(" ", "") + "\n"
                f_new.write(line)
                f_new.flush()
    os.replace("cus_info.dat", "cus_info_bank.txt")


# 卖家登录方法
def login_sel(username, password):
    with open("sel_info.txt", "r", encoding="utf-8") as f_sel_info:
        for line in f_sel_info:
            _line = line.strip().split(",")
            if username == _line[0]:
                if password == _line[1]:
                    print(str_login_suc % username)
                    return "1"
                else:
                    return "0"
        print(str_login_not_exist)
        return "2"

#修改商品列表方法 type=1 删除，type=2 修改
def edit_product(type,num,product,price):
    with open("shoppingmall_list.txt", "r", encoding="utf-8") as f_product_list:
        with open("shoppingmall_list.bak", "w", encoding="utf-8") as new_file:
            count = 0
            for line in f_product_list:
                _line = line.split(",")
                count += 1
                if count==int(num):
                    if type==1:
                        line=""

                    if type==2:
                        line=product+","+price+"\n"
                new_file.write(line)
                new_file.flush()
    os.replace("shoppingmall_list.bak","shoppingmall_list.txt")






while switch_mail:
    choice_system = input("1.买家系统\n2.卖家系统\n请选择您要登录的系统：")
    if choice_system == "1":
        username = input(str_username)
        password = input(str_password)
        # 执行登录方法，登录成功返回结果1
        login_result = login_cus(username, password)
        if login_result[0] == "1":
            balance = int(login_result[1])
            while switch_choice_product:
                print("您的余额为：", balance)
                # 执行展示商品目录方法
                total = product_list()
                cus_choice = input(str_choice_product)
                if cus_choice.isdigit() and int(cus_choice) <= total:
                    with open("shoppingmall_list.txt", "r", encoding="utf-8") as f_product_list:
                        count = 0
                        for line in f_product_list:
                            count += 1
                            if int(cus_choice) == count:
                                _line = line.strip().split(",")
                                if balance - int(cus_choice) >= 0:
                                    balance = balance - int(_line[1])
                                    # 输出购买的产品信息
                                    print("您购买的商品为：", _line[0], _line[1])
                                    # 修改买家余额
                                    modify_balance(username, balance)
                                    # 执行更改购买商品清单
                                    modify_shopping_list(username, _line[0], _line[1])
                                else:
                                    print("当前余额不足，请充值！")

        else:
            print(str_wrong_msg)

    elif choice_system == "2":
        username = input(str_username)
        password = input(str_password)
        login_result = login_sel(username, password)
        if login_result[0] == "1":
            while switch_product:
                print("以下是商品信息：")
                product_list()
                input_order = input(str_product_order + "请输入您要操作的指令：")
                order = input_order.split(",")
                if order[0] == "add" and len(order) == 3:
                    with open("shoppingmall_list.txt","a+",encoding="utf-8") as f_product_list:
                        f_product_list.write("\n"+order[1]+","+order[2])
                        print("您已成功添加："+order[1]+","+order[2]+"到商品列表")

                elif order[0] == "del" and len(order) == 2:
                    edit_product(1, order[1],"","")
                    print("删除成功")
                elif order[0] == "edit" and len(order) == 4:
                    edit_product(2,order[1],order[2],order[3])
                    print("您已成功修改："+order[2]+","+order[3]+"到商品列表")
                else:
                    print("您输入的指令有误！")
    else:
        print(str_wrong_msg)
