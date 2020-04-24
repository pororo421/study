#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/20 23:09
# @File: test.py
# @Software: PyCharm

def calcu(B):
    G=int(((B/1024)/1024)/1024)

    print(G)
calcu(2**32)
calcu(2**64)


