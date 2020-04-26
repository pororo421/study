#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/18 10:25
# @File: file_modify.py
# @Software: PyCharm
f =open("file.txt","r",encoding="utf-8")
f_new=open("file_new.txt","w",encoding="utf-8")

for line in f:
    if "能否记起"in line:
        line=line.replace("能否记起","-----能否记起----")
    f_new.write(line)
    f_new.flush()
f.close()
f_new.close()
