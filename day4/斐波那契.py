# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/25 15:31
# @File: 斐波那契.py
# @Software: PyCharm
def feib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
        print("n,a,b=", n, a, b)
    return "done"


f = feib(10)

while True:
    try:
        x=next(f)
        print("f:",x)
    except StopIteration as e:
        print("Generator return value:",e.value)
        break

# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())




# print("-------fengexian------")
# for i in f:
#     print(i)

# x = (i * 2 for i in range(10))
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())