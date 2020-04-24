#-*- coding:utf-8 -*-
#  @Author  :pororo
#  @Time    :2020-04-24 下午 15:50
#  @Note    :
import time
def bar():
    time.sleep(2)
    print("in the bar")
def test1(func):
    print(func)
    func()
test1(bar)
t=test1(bar)
print(t)
