# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/20 15:51
# @File: 局部变量.py
# @Software: PyCharm
age = "jmy"
def change_name():
    print("changename:", age)
    # age = "meiyan"     #这个函数就是这个变量的作用域
    print("修改后：", age)



change_name()
print(age)
