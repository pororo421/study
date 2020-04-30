#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/8 0:23
# @File: pass.py
# @Software: PyCharm

import getpass
_username="jmy"
_password="666"
username= input("username:")
password= input("password:")

#print(username,password)
if _username==username and _password==password:
    print("欢迎{name}登录".format(name=username))
else:
   print("无效的用户名或密码")