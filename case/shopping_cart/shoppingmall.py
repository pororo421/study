# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/14 23:01
# @File: shoppingmall.py
# @Software: PyCharm
import os

str_cus_choice = "c"
str_sel_choice = "s"
str_login = "which system do you want to login?\n\033[34mc.custmer\ns.Seller\033[0m\nyour choice:"
str_welcome_cus = "\033[5;35m welcome! \033[0m "
str_welcome_sel = "\033[33m welcome!\033[0m"

str_choice_wrong = "\033[31m Your choice is not exist ,please try again!\033[0m"
str_cus_username = "please enter your username:"
str_cus_password = "please enter your password:"
str_sel_username = "please enter your username:"
str_sel_password = "please enter your password:"
str_cmd = '''
操作指南：
删除：d,产品编号 （例：d,2)
添加：a,产品名称,价格（例：a,samsung,1000）
修改：m,序号,产品名称,价格 （例：m,2,sansumg1,999）
\033[33m请选择指令\033[0m：
'''
delete = "d"  # 删除操作
add = "a"  # 添加操作
modify = "m"  # 修改操作
is_login = True
is_sel_choice = True
is_cus_login = True
cus_exist = 0  # 1时用户存在，0时用户不存在
is_cus_buy = True
balance = 0


# 用户登录
def func_login(cus_username, cus_password):
    with open("cus_info.txt", "r", encoding="utf-8") as cus_info_file:
        for line in cus_info_file:
            _line = line.strip().split(",")
            if cus_username == _line[0]:
                if cus_password == _line[1]:
                    print("hello!", cus_username, ",Here is your product list:")  # 用户登录成功
                    balance = int(_line[2])
                    return 1, balance
                else:
                    print("您输入的密码有误，请重新输入！")
                    return 0
        print("用户不存在！")
        return 2

# 展示商品列表
def shopping_list():
    with open("shoppingmall_list.txt", "r", encoding="utf-8") as product_list:
        index = 0
        for line in product_list:
            index += 1
            print(index, line)

# 修改用户购买列表
def modify_cus_shoppinglist(username, product, price):
    with open("shopping_list.txt", "r", encoding="utf-8") as file_shopping_list:  # 用户购买的列表
        with open("new_shopping_list.txt", "w", encoding="utf-8") as new_file:
            for line in file_shopping_list:
                list = line.split(":", 1)
                user = list[0]
                if user == cus_username:
                    shopping_list = list[1].replace("[", "").replace("]", "").replace('"', "").split(",")
                    shopping_list.append(product, "-", price)
                    line = username + ":" + str(shopping_list)

                new_file.write(line)
                new_file.flush()
    os.replace("new_shopping_list.txt", "shopping_list.txt")

# 修改余额
def modify_balance(cus_username, new_balance):
    with open("cus_info.txt", "r", encoding="utf-8") as cus_file:
        with open("cus_info.txt", "w", encoding="utf-8") as new_file:
            for line3 in cus_file:
                _line3 = line3.strip().split(",")
                if cus_username in _line3:
                    line3 = str(_line3).replace(_line3[2], str(new_balance))
                    line3 = line3.replace("[", "").replace("]", "").replace(" ", "").replace("'", "") + "\n"
                new_file.write(line3)
                new_file.flush()
    os.replace("cus_info.txt", "cus_info.txt")  # replace(原文件，目标文件

while is_login:
    choice_system = input(str_login)
    if choice_system == str_cus_choice:
        print(str_welcome_cus)
        while is_cus_login:
            cus_username = input(str_cus_username)
            cus_password = input(str_cus_password)
            login_result = func_login(cus_username, cus_password)
            if login_result == 0:
                pass
            elif login_result == 2:
                pass
            elif login_result[0] == 1:
                shopping_list()
                while is_cus_buy:
                    balance = login_result[1]
                    cus_choice_item = input("your balance:" + str(balance) + "\n" + "Which item do you want to buy?")
                    count = 0
                    with open("shoppingmall_list.txt", "r", encoding="utf-8") as product_list:
                        for line2 in product_list:
                            _line2 = line2.strip().split(",")
                            count += 1
                            if int(cus_choice_item) == count:
                                print(_line2)
                                if balance >= int(_line2[1]):  # 判断余额是否大于商品金额
                                    modify_balance(cus_username, balance)
                                    modify_cus_shoppinglist(cus_username, _line2[0], _line2[1])

    elif choice_system == str_sel_choice:
        print(str_welcome_sel)
        sel_username = input(str_sel_username)
        sel_password = input(str_sel_password)
        with open("sel_info.txt", "r", encoding="UTF-8") as sel_info:
            # with open("w+","sel_info.txt")as sel_info:
            for index, line in enumerate(sel_info.readlines()):
                index += 1
                sel_line = line.split(",")
                # print(index, ".", "用户名：", sel_line[0], "密码：", sel_line[1])
                if sel_username == sel_line[0] and sel_password == sel_line[1].strip("\n"):
                    print("hello!", sel_line[0], ",Here is your product list:")
                    with open("shoppingmall_list.txt", "r", encoding="UTF-8") as product_list:
                        for index, pro_line in enumerate(product_list.readlines()):
                            pro_line = pro_line.split(",")
                            # print(index + 1, ".", "brand:", pro_line[0], "price:", pro_line[1])
                    with open("shoppingmall_list.txt", "r", encoding="UTF-8") as list:
                        for index, product in enumerate(list.readlines()):
                            print(index + 1, ".", product)

                    while is_sel_choice:
                        _product = input(str_cmd)
                        new_file = ""
                        with open("shoppingmall_list.txt", "r", encoding="UTF-8") as del_list:
                            # for index, product in enumerate(del_list.readlines()):
                            cmd = _product.split(",")
                            if cmd[0] == delete and len(cmd) == 2:
                                for index, product in enumerate(del_list.readlines()):
                                    if cmd[1] == str(index + 1):  # 判断商家选择删除的产品是否在产品列表里 是：删除该产品
                                        new_file = new_file + ""  # 将要删除的产品赋予空值
                                        continue
                                    new_file = new_file + product
                            elif cmd[0] == add and len(cmd) == 3:
                                with open("shoppingmall_list.txt", "a+", encoding="utf-8") as add_list:
                                    add_list.write("\n" + cmd[1] + "," + cmd[2])


                            elif cmd[0] == modify and len(cmd) == 4:
                                # with open("shoppingmall_list.txt","r",encoding="utf-8") as mod_list:
                                for index, product in enumerate(del_list.readlines()):
                                    if cmd[1] == str(index + 1):
                                        new_file = new_file + cmd[2] + "," + cmd[3] + "\n"
                                        continue
                                    # for line in mod_list:

                                    new_file = new_file + product
                            else:
                                print("您输入的指令有误！")
                        if cmd[0] == delete or cmd[0] == modify:  # 判断用户输入的指令是否为删除
                            with open("shoppingmall_list.txt", "w", encoding="UTF-8") as new_list:
                                # print(new_file)
                                new_list.write(new_file)
            break
    else:
        print(str_choice_wrong)
