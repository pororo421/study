#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/20 14:48
# @File: canshu.py
# @Software: PyCharm
#
# def test(x,y=2):
#     print(x)
#     print(y)
#
# test(1,y=5)
# #默认参数特点： 调用函数的时候，默认参数非必须传递
# #用途：默认值
#
#
# # *表示要定义的参数个数不固定
# def tes1(*args):
#     print(args)
#
# test1(1,2,3,5)
# test1(*[1,2,3,5])  #args=tuple([1,2,3,5])
#
# def test2(x,*args):
#     print(x)
#     print(args)
# test2(1,2,3,7,8,9)

# #接收字典 **kwargs 把N个关键字参数转换成字典的方式
# def test3(**kwargs):
#     print(kwargs)
#     print(kwargs["name"])
#     print(kwargs["age"])
# test3(name="acv",age=33,sex="F")
# test3(**{"name":"scv","age":8})

# def test4(name,**kwargs):
#     print(name)
#     print(kwargs)
# test4("acv",age=2,sex="m")

# print(sep="")
# print("a","b","c","d")
# print("a","b","c","d",sep="-")

# def test5(name,age=90,*args,**kwargs):
#     print(name)
#     print(age)
#     print(args)
#     print(kwargs)
# test5("axc",12,3,15,sex="m",hobby="sdf")
def test(*args):
    print(args)
test(123,23,24)




