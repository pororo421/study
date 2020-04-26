#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/17 23:59
# @File: 进度条.py
# @Software: PyCharm

import  sys,time
for i in range(50):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.5)