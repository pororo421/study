# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/20 16:17
# @File: 全局变量局部变量.py
# @Software: PyCharm

school = "qinghua"
def change_school():
    global school
    print("xiugaiqian:", school)
    school = "beida"
    print("xiugaihou:", school)
change_school()
print(school)
