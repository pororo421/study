#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/22 12:58
# @File: test-shoppinglist.py
# @Software: PyCharm
import os

def modify_cus_shoppinglist(username, product, price):
    with open("shopping_list.txt", "r", encoding="utf-8") as file_shopping_list:  # 用户购买的列表
        with open("new_shopping_list.txt", "w", encoding="utf-8") as new_file:
            for line in file_shopping_list:
                list = line.split(":", 1)
                user = list[0]
                if user == username:
                    shopping_list1 = list[1].replace("[", "") #.replace("]", "").replace('"', "").replace("\n","").split(",")
                    print("去掉[符号：",shopping_list1)
                    shopping_list2=shopping_list1.replace("]", "")
                    print("去掉]符号：",shopping_list2)
                    shopping_list3=shopping_list2.replace('"', "")
                    print("去掉双引号：",shopping_list3)
                    shopping_list4=shopping_list3.replace("\n","")
                    print("去掉回车：", shopping_list4)
                    shopping_list5=shopping_list4.split(",")

                    shopping_list5.append(product+":"+ str(price))
                    line = username + ":" + str(shopping_list5)+"\n"
                    # line=line.replace("'",'"').replace(" ","")

                new_file.write(line)
                new_file.flush()
    os.replace("new_shopping_list.txt", "shopping_list.txt")
modify_cus_shoppinglist("cus1","iphone",2000)
