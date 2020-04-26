# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/14 9:52
# @File: shoppingCart_new.py
# @Software: PyCharm

goods = [("iphone", 5000), ("samsung", 4000), ("huawei", 3000), ("xiaomi", 2000)]

is_choice = True
shopping_list = []
exit_menu = "w"
balance = input("请输入您的工资:")
if balance.isdigit():
    balance = int(balance)
    while is_choice:
        for index, product in enumerate(goods):
            print(index, product)
        cus_choice = input("请选择您要购买的商品（如需退出请输入%s）：" % (exit_menu))
        if cus_choice == exit_menu:
            print("购物清单".center(50, '-'))
            for list in shopping_list:
                print(list),
            print("余额为：\033[31;1m%s\033[0m" %(balance))
            exit()
        elif cus_choice.isdigit():
            cus_choice = int(cus_choice)
            if cus_choice >= 0 and cus_choice < len(goods):
                cus_choice = int(cus_choice)
                _brand = goods[cus_choice]
                if _brand[1] <= balance:
                    shopping_list.append(_brand)
                    balance = balance - _brand[1]
                    print("您的购买的商品为 %s , 余额为\033[31;1m%s\033[0m " % (_brand, balance))
                else:
                    print("\033[31;47m您的余额不足！\033[0m")
        else:
            print("您输入的商品不存在！")
