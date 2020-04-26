 #-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/26 15:02
# @File: json序列化.py
# @Software: PyCharm
# import 内置方法 as neizhi
# neizhi.get_username("qlt")
import pickle
# import json

# info={
#      "name":"qlt",
#      "age":12
#  }
# with open("test.txt","w",encoding="utf-8") as new_file:
#     new_file.write(json.dumps(info))

def sayhello(name):
    print("您好！",name)
info={
     "name":"qlt",
     "age":12,
     "方法":sayhello
 }
with open("test.txt","wb") as f:
    # f.write(pickle.dumps(info))
    pickle.dump(info,f)