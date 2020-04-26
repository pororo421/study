# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/17 16:09
# @File: set.py
# @Software: PyCharm

list_1 = [1, 5, 2, 6, 3, 5, 9]
list_1 = set(list_1)
list_2 = [2,3,9,58,1,5]
list_2=set(list_2)
list_3=[52,7]
list_4=[2,3,56,4,3,45]

# print(list_1, type(list_1))
#交集
print((list_1.intersection(list_2)))
print(list_1&list_2)
#并集
print(list_1.union(list_2))
print(list_1|list_2)
#差集 在list_1里，但list_2里没有
print(list_1.difference(list_2))
print(list_1-list_2)
#子集
print(list_1.issubset(list_2))
#父集
print(list_1.issuperset(list_3))
#对称差集
print(list_1.symmetric_difference(list_2))
print(list_1^list_2)
#没有交集
print(list_1.isdisjoint(list_3))
#添加一项
list_1.add(20)
print(list_1)
#添加多项
list_1.update([10,20,30])
#删除
list_1.remove(1)
#len(s)
#set 的长度

#x in s