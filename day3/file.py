#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/17 16:39
# @File: file.py
# @Software: PyCharm
f =open("file.txt","r",encoding="utf-8")
'''
读前5行语法
for i in range(5):
    print(f.readline())
'''

'''
一行一行读文件，并且只存一行，读一行覆盖一行
for line in f:
print(line)
'''
'''
# 读前10行
count =0
for line in f:
    if count==9:
        print("--------分割线-----")
        count +=1
        continue
    print(line.strip())
    count +=1
'''

print(f.tell()) #光标位置
print(f.readline()) #读一行
print(f.tell()) #第一行的字符个数
print(f.read(5))
print(f.tell())

f.seek(0)    #光标回到0的位置
print(f.readline())