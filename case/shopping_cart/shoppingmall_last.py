# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/20 9:41
# @File: shoppingmall_last.py
# @Software: PyCharm
import os

is_login = True
is_cus_login = True
is_cus_buy = True
str_cus_login = "c"
str_sel_login = "s"
str_login = "Which system do you want to login?\n\033[34mc.custmer\ns.Seller\033[0m\nyour choice:"
str_welcome = "\033[33m Welcome!\033[0m"
str_pass_wrong = "\033[31mThe password you entered is incorrect,please try again!\033[0m "
str_user_not_exist = "\033[31mUser does not exist\033[0m "

str_cus_username = "please enter your username:"
str_cus_password = "please enter your password:"
str_sel_username = "please enter your username:"
str_sel_password = "please enter your password:"
balance = 0


# 用户登录方法
def cus_login_func(cus_username, cus_password):
    with open("cus_info.txt", "r", encoding="utf-8") as f_cus_info:
        for line in f_cus_info:
            _line = line.strip("").split(",")
            if cus_username == _line[0]:
                if cus_password == _line[1]:
                    print("hello!", cus_username, ",Here is your product list:")  # 用户登录成功
                    balance = int(_line[2])
                    # print(balance)
                    return 1, balance
                else:
                    print(str_pass_wrong)
                    return 0
        print(str_user_not_exist)
        return 2


# 展示商品列表
def shopping_list():
    with open("shoppingmall_list.txt", "r", encoding="utf=8") as f_product_list:
        index = 0
        for line in f_product_list:
            index += 1
            print(index, line)


# 购买后的余额
def modify_balance(cus_username, balance):
    with open("cus_info.txt", "r", encoding="utf-8") as f_cus:
        with open("new_cus_info.txt", "w", encoding="utf-8") as f_new:
            for line in f_cus:
                _line = line.strip().split(",")
                if cus_username in _line:
                    line = str(_line).replace(_line[2], str(balance))
                    line = line.replace("[", "").replace(" ", "").replace("]", "").replace("'", "") + "\n"
                f_new.write(line)
                f_new.flush()
    os.replace("new_cus_info.txt", "cus_info.txt")


# 修改商品列表
def modify_cus_shoppinglist(username, product, price):
    with open("shopping_list.txt", "r", encoding="utf-8") as file_shopping_list:  # 用户购买的列表
        with open("new_shopping_list.txt", "w", encoding="utf-8") as new_file:
            for line in file_shopping_list:
                list = line.split(":", 1)
                user = list[0]
                if user == username:
                    shopping_list = list[1].replace("[", "").replace("]", "").replace('"', "").replace("\n","").split(",")
                    shopping_list.append(product+":"+ price)
                    line = username + ":" + str(shopping_list)+"\n"
                    line=line.replace("'",'"').replace(" ","")
                    line=line.replace("'").replace(" ","")

                new_file.write(line)
                new_file.flush()
    os.replace("new_shopping_list.txt", "shopping_list.txt")


# 选择登录接口
while is_login:
    choice_system = input(str_login)
    if choice_system == str_cus_login:
        print(str_welcome)
        while is_cus_login:
            cus_username = input(str_cus_username)
            cus_password = input(str_cus_password)
            cus_login_result = cus_login_func(cus_username, cus_password)
            # cus_login_result  （ result[0]->=0时密码错误，=1时登录成功，=2时用户不存在,result[1]->balance）
            if cus_login_result[0] == 1:
                shopping_list()
                balance = cus_login_result[1]
                while is_cus_buy:
                    cus_choice_item = input("Your balance:" + str(balance) + "\n" + "Which item do you want to buy?")
                    count = 0
                    with open("shoppingmall_list.txt", "r", encoding="utf-8") as f_product_list:
                        for line in f_product_list:
                            _line = line.strip().split(",")
                            count += 1
                            if count == int(cus_choice_item):
                                print(_line)
                                if balance >= int(_line[1]):
                                    balance=balance-int(_line[1])
                                    print("购买后的余额：",balance)
                                    modify_balance(cus_username, balance)
                                    modify_cus_shoppinglist(cus_username, _line[0], _line[1])
