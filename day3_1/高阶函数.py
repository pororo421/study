#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/20 22:41
# @File: 高阶函数.py
# @Software: PyCharm
a=1
b=2
def add():
    # z=x+y
    # print("z等于:",z)
    return 3

def minus(z,y):
    q=z-y
    print("q等于：",q)
minus(add,b)
