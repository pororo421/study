# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/13 16:36
# @File: shopping_cart_qlt.py
# @Software: PyCharm
item = [[1, "samsung", 6000], [2, "iphone", 5000], [3, "huawei", 4000], [4, "xiaomi", 3000]]
balance = int(input("请输入您的工资"))
quit = 0
num = 1
shopping_cart = []
swich = True
while swich:
    for phone in item:
        print("{_num}.{_phone}:{_price}".format(_num=phone[0], _phone=phone[1], _price=phone[2]))
    input_menu = int(input("请输入需要购买的商品"))
    if input_menu == quit:
        print("您的购物清单是：{_shopping_cart}，余额为：{_balance}".format(_shopping_cart=shopping_cart, _balance=balance))
        swich = False
        break
    elif input_menu > 0 and input_menu <= len(item):
        input_menu = input_menu - 1
        _balance = balance - item[input_menu][2]
        if _balance >= 0:
            balance = _balance
            print("{_item}：价格{_price}购买成功!余额为{_balance}".format(_item=item[input_menu][1], _price=item[input_menu][2],
                                                                _balance=balance))
            shopping_cart.append(item[input_menu])
        else:
            print("余额不足！")
    else:
        print("您的输入有误，请重新输入！")

