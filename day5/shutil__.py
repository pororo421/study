#-*- coding:utf-8 -*-
#  @Author  :pororo
#  @Time    :2020-04-30 下午 14:27
#  @Note    :
import shutil
import zipfile
import datetime
import shelve
# f1= open("test.py",encoding="utf-8")
# # f2= open("test2.py","w",encoding="utf-8")
# #
# #
# # shutil.copyfileobj(f1,f2)

# shutil.copyfile("test2.py","test3.py")
# shutil.make_archive("D:\workspace\python\pororo\study\day6\\test6","zip","D:\workspace\python\pororo\study\day5")


#压缩
# z=zipfile.ZipFile("day5_2.zip","w")
# z.write("test2.py")
# z.write("test3.py")
# z.close()

#解压
# z=zipfile.ZipFile("day5_2.zip","r")
# z.extractall("test")
# z.close()

d=shelve.open("shelve_test")
# info={"age":22,"job":"it"}
# name=["a","b","c"]
# d["name"]=name
# d["info"]=info
# d["date"]=datetime.datetime.now()
print(d.get("name"))
print(d.get("info"))
print(d.get("date"))
# d.close()