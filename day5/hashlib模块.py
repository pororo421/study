#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-30 下午 17:05
#  @Note    :
import hashlib

m=hashlib.md5()
m.update(b"hello")
print(m.hexdigest())
m.update(b"It's me")
print(m.hexdigest())