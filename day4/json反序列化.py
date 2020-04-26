#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/26 15:18
# @File: json反序列化.py
# @Software: PyCharm
import pickle
def sayhello(name):
    # print("您好",name)
    print("hello",name)
with open("test.txt", "rb") as new_file:

    # data=pickle.loads(new_file.read())
    data=pickle.load(new_file)

    print(data["方法"]("qlt"))
