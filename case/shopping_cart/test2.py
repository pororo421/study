#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/19 23:08
# @File: test2.py
# @Software: PyCharm
s='cus1: ["xiaomi:3000", "huawei:2000"]'
s1=s.split(":",1)
print(s1[1])
s_list=s1[1].split(",")
s_list.append("iphone:6000")
print(s_list)