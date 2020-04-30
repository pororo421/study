# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/19 12:03
# @File: test1.py
# @Software: PyCharm

    def list():
        with open("shoppingmall_list.txt", "r", encoding="utf-8") as pro_list:
            pro_list.write(test_file)
list()


def modify_balance(cus_username, new_balance):
    with open("cus_info.txt", "r", encoding="utf-8") as f_cus:
        with open("cus_info.txt", "r", encoding="utf-8") as f_new:
            for line in f_cus:
                _line = line.strip().split(",")
                if cus_username in _line:
                    line = str(_line).replace(_line[2], str(new_balance))
                    line = line.replace("[", "").replace(" ", "").replace("]", "").replace("'", "") + "\n"
                    f_new.write(line)
                    f_new.flush()
    os.replace("cus_info_bank.txt", "cus_info_bank.txt")


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


4.
elif cus_login_result == 0:
pass
elif cus_login_result == 2:
pass
