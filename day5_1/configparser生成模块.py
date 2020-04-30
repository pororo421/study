#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-30 下午 16:28
#  @Note    :
import  configparser

config=configparser.ConfigParser()
config.read("exanple.ini",encoding="utf-8")
# config["Default"]={
#     "最小内存":"256M",
#     "最大内存":"512M"
# }
# config["info"]={}
# config["Default"]["forwardx11"]="yes"

# with open("exanple.ini","w",encoding="utf-8") as configfile:
#     config.write(configfile)
print(config["Default"])
