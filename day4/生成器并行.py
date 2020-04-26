#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/25 16:51
# @File: 生成器并行.py
# @Software: PyCharm
import  time
def chibaozi(name):
    print("%s准备吃包子了"%name)
    while True:
        baozi=yield
        print("包子[%s]来了，被[%s]吃了"%(baozi,name))
    return "没有包子"
f=chibaozi("全林天")
f.__next__()

b1="韭菜馅"
f.send(b1)
f.__next__()

def fenbaozi():

    user1=chibaozi("全林天")
    user2=chibaozi("全夏岚")

    print("开始做包子了")
    for i in range(10):
        time.sleep(1)
        print("做了两个包子！")
        user1.send(i)
        user2.send(i+1)




