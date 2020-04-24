#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/20 16:40
# @File: 递归.py
# @Software: PyCharm
# def digui(n):
#     print(n)
#     return digui(n+1)
# digui(0)
count=0
def digui(n):
    print(n)

    if int(n/2)>0:
        global count
        count+=1
        print("count"+str(count))
        return digui(int(n/2))
digui(2**10)



