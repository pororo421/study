#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/8 1:11
# @File: guess.py
# @Software: PyCharm

age_of_tom=20
count = 0
#while True:
for i in range(3):
    if count ==3:
        break
    guess_age=int(input("guess age:"))

    if age_of_tom==guess_age:
        print("恭喜你猜对了！")
        break
    elif age_of_tom>guess_age:
        print("没那么老")
    else:
        print("哪有那么年轻")

   # count = count+1



