#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/13 14:24
# @File: tuple.py
# @Software: PyCharm

import copy
# print("1")

while True:
    a= input("请输入：")
    if a.isdigit():
        print(a,"的数据类型为数字\033[31;47m\033[0m")
    else:
        print(a,"的数据类型为字符串")