# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/18 14:57
# @File: 函数.py
# @Software: PyCharm
'''
import time
def logger():
    time_format='%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open("file.txt","a+")as f:
        f.write("time %s end action"%time_current)
logger()



def test1():
    pass
def test2():
    return 0
def tesr3():
    return 1
def test4():
    return 5,"hjhj",["safs","sfs"],{"safs":"8dfsd"}
t1=test1()
t2=test2()
t3=tesr3()
t4=test4()
print ('from test1 return is [%s]:'%type(t1),t1)
print ('from test2 return is [%s]:'%type(t2),t2)
print ('from test3 return is [%s]:'%type(t3),t3)
print ('from test4 return is [%s]:'%type(t4),t4)
'''


def test(x, y,z):  # x,y 为形参
    print(x)
    print(y)
    print(z)


test(1, 2,3)  # 与形参顺序一一对应    1,2 为实参
test(y=2, x=1,z="3")  # 与形参顺序无关
