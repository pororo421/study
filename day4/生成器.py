#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/25 0:29
# @File: 生成器.py
# @Software: PyCharm
import time,sys
a =[i*2 for i in range(100000)]
print(a)
b=( i*2 for i in range(10000))

def timera():
    start=time.time()
    a=[i*2 for i in range(10000000)]
    stop=time.time()
    print("a耗时：",(stop-start))
    print(sys.getsizeof(a))


def timerb():
    start = time.time()
    b = (i * 2 for i in range(10000000))
    stop = time.time()
    print("b耗时：", (stop - start))
    print(sys.getsizeof(b))


timera()
timerb()