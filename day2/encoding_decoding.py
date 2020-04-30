#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/13 9:18
# @File: encoding_decoding.py
# @Software: PyCharm

# encode   编码  str转换成 bytes
# decode  解码

msg= "全林天看手机"
print(msg)
print(msg.encode(encoding="utf-8"))
print(msg.encode(encoding="UTF-8").decode(encoding="UTF-8"))

print(type(2**64))
print(type(100**10000))


'''
import os
cmd_res= os.system("dir")  #执行命令，不保存结果
cmd_res= os.popen("dir").read() #执行命令，保存结果
print("输出", cmd_res)
'''
import os
day03= os.path.isdir("../day3")
if day03 is False:
    os.makedirs("../day3")