#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/20 15:42
# @File: 方法里调用方法.py
# @Software: PyCharm

def login(username):
    print(username)
def test(name,age=99):
    print(name)
    print(age)
    login(name)

test("user01")


