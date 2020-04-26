#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/25 22:20
# @File: 迭代器.py
# @Software: PyCharm

# for x in range(10):
#     print(x)

it=iter([1,2,3,4,5,6,7,8,9,10])
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break

