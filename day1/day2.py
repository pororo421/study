#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/7 16:35
# @File: day2.py
# @Software: PyCharm

'''
print("hello world!")

name = " Meiyan Jin"
name2 = " rg"
print("My name is", name,name2)
'''

'''
username= input("username:")
password= input("password:")
print(username,password)
'''

name= input("name")
age= str(int(input("age")))
print(type(age))
job=input("job")
salary=input("salary")
# info= '''
# info of %s
# name:%s
# age:%d
# job:%s
# salary:%s
# ''' %( name,name,age,job,salary)


# info2='''
# info of {_name}
# name:{_name}
# age:{_age}
# job:{_job}
# salary:{_salary}
# ''' .format(_name=name,_age=age,_job=job,_salary=salary)
# print(info2)

info3='''
info of {0}11
name:{0}
age={1}
job={2}
salary={3}
'''.format(name,age,job,salary)
print(info3)