#-*- coding:utf-8 -*-
#  @Author  :PORORO421
#  @Time    :2020-04-24 下午 15:35
#  @Note    :
import  time,datetime
def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print("the func run time is %s"%(stop_time-start_time))
    return warpper
@timmer
def login():
    time.sleep(2)
    print("time:",datetime.datetime.now())

login()