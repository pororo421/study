# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/13 14:49
# @File: shopping_cart.py
# @Software: PyCharm

goods = [[1, "iphone", 5000], [2, "samsung", 4000], [3, "huawei", 3000], [4, "xiaomi", 2000]]

exit_menu = "0"
shopping_list=[]
is_choice = True
balance = input("您的工资为：")
while is_choice:

    for choice in goods:
        print(choice)
    cus_choice = input("请选择您要购买的商品（如需退出请输入0）：")
    if cus_choice == exit_menu:
        print("您购买的商品为：, {_shopping_list},余额为：,{_balance}".format(_shopping_list= shopping_list, _balance=balance))
        is_choice=False
        break
    elif int(cus_choice)>=0 and int(cus_choice)<= len(goods):
        cus_choice= int(cus_choice) - 1
        _num = goods[int(cus_choice)][0]
        _brand = goods[int(cus_choice)][1]
        _price = goods[int(cus_choice)][2]
        _balance = int(balance) - _price
        if _balance >= 0:
            balance=_balance
            print("您购买的商品为:", _brand, "余额为:", _balance)
            shopping_list.append(goods[int(cus_choice)])
        else:
            print("您的余额不足，无法购买该商品，如需退出请输入0")
    else:
        print("您的输入有误，请重新输入！")


