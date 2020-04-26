# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/25 23:18
# @File: 内置方法.py
# @Software: PyCharm
# print(all([2,3,4]))
# print(any([0,2,3,4]))
# print(bool(0))
# print(bool(1))
# a=bytes("你好",encoding="utf-8")
# b=bytearray("yui",encoding="utf-8")
# # print(a.decode("utf-8"))
# # print(b.decode("utf-8")[0])
# b[1]=97
# print(b.decode("utf-8"))

# res=filter(lambda n:n>5,range(10))
# res=map(lambda n:n>5,range(10))
# res=[lambda  i:i*2 for i in range(10)]
# for i in res:
#     print(i)

# a = {4: 33, 5: 22, 9: 45, 3: 566, 1: 45}
# print(sorted(a.items()))
# print(sorted(a.items(),key=lambda x:x[1]))
# print(sorted(a.items(),key=lambda x:x[0]))

#zip
# a=[1,2,3,4,5,]
# b=['a','b','c','d','e','f','g']

#     for i in zip(a,b):
#         print(i)
#
# def get_username(name):
#     print(name)
#

