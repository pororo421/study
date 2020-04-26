# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/24 22:17
# @File: 装饰器+高阶函数.py
# @Software: PyCharm
import time


def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        a="lisi"
        b="22"
        func(a, b)
        stop_time = time.time()
        print("运行方法耗时%s" % (stop_time - start_time))

    return deco


@timer
def test1():
    time.sleep(2)
    print("in the test1")
@timer
def test2(name, age):
    print("test2:", name, age)
# test1()
test2()
