#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/22 17:09
# @File: test.py
# @Software: PyCharm
# name="pororo"
# name2=name
# print(name,name2)
#
# name="RG"
# print("What's the value of name2 now?",name2)
#
import getpass
name=input("请输入用户名：")
password=getpass.getpass("请输入密码：")
print(password)

# import sys
#
# print(sys.argv)
#
# name="Tom"
# print("I'am %s"%name)
# name_list=["tom","jelly","jean","alice"]
# name_list=list(["tom","jelly","jean","alice"])
#
#
# name=input("请输入用户名：")
# password=input("请输入密码：")
# if name=='tom' and password=='123':
#     print("欢迎",name)
# else:
#     print("您输入的用户名与密码有误！")