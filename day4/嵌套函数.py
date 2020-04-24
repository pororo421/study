#-*- coding:utf-8 -*-
#  @Author  :pororo
#  @Time    :2020-04-24 下午 16:16
#  @Note    :
def foo():
    print('in the foo')
    def bar():
        print('in the bar')
    bar()
foo()