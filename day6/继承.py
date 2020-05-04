#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/5/4 22:00
# @File: 继承.py
# @Software: PyCharm

#python2 里经典类是按深度优先继承的，新式类是按广度优先继承
#python3 里经典类与新式类都是按广度优先继承的


# 经典类
#class people
class people(object):  #新式类
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.friends=[]
    def eat(self):
        print("%s is eating"%self.name)
    def sleep(self):
        print("%s is sleeping"%self.name)
class relation(object):
    def make_friends(self,object):
        print("%s is fall in love with %s"%(self.name,object.name))
        self.friends.append(object.name)

class man(people,relation):
    # 新增加一个属性money，此时需要把父类的属性name与age也加上

    def __init__(self,name,age,money):
        # 方法1：
        # people.__init__(self,name,age)
        # 方法2：
        super(man,self).__init__(name,age)
        self.money=money
    def money1(self):
        print(" 出生就有%s" %self.money)


    def work(self):
        print("%s is working"%self.name)

    def sleep(self):
        people.sleep(self)
        print("He is realy sleeping")
class woman(people,relation):
    def shopping(self):
        print("%s is shopping"%self.name)
m1=man("qlt",20,1)
# m1.eat()
# m1.work()
# m1.sleep()
# m1.money1()
w1=woman("jmy",12)
# w1.shopping()
m1.make_friends(w1)
w1.name="qxl"
print(m1.friends[0])