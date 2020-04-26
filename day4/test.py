#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/26 22:51
# @File: test.py
# @Software: PyCharm
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for index,i in enumerate(a):
    a[index] +=1
print(a)

a = map(lambda x:x+1, a)
print(a)
for i in a:print(i)

a = [i+1 for i in range(10)]
print(a)