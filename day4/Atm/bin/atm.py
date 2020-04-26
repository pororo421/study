#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/26 16:24
# @File: atm.py
# @Software: PyCharm
import os
import sys
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
# import conf,core

from conf import settings
from core import main
main.login()