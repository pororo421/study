#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/22 22:14
# @File: shopping_mall_qlt.py
# @Software: PyCharm
import os

str_wrong_msg = "您输入有误，请重新输入！"
str_input_username = "请输入用户名："
str_input_password = "请输入密码："
str_login_ok = "欢迎%s登陆成功！"
str_login_fail = "账号与密码不匹配，请重新输入！"
str_user_not_exist = "此用户不存在！"
str_item_order = '''
1.添加(命令:add,商品名,价格)                 e.g : add,iphone7,5000
1.修改(命令:edit,商品序号,新商品名，新价格)   e.g : edit,1,iphone7,5000
1.删除(命令:del,商品序号)                    e.g : del,1
请输入您要操作的指令：
'''
switch_main = True #整个程序开关
switch_item = True #商品列表开关
switch_buy_item = True #购买商品开关

#余额默认为0
balance = 0

#登录方法
#type = 1.买家登录,type=2卖家登录,type=3.安卓用户登录,type=4苹果用户登录
#成功返回1，失败返回0
def login_cus(username,password,type):
    with open("cus_info.txt","r",encoding="utf-8") as userinfo:
        for line in userinfo:
            _line = line.strip().split(",")
            if username == _line[0]:
                if password == _line[1]:
                    print(str_login_ok %username)
                    return "1",_line[2]
                else:
                    print(str_login_fail)
                    return "0"
        print(str_user_not_exist)
        return "0"

#登录方法
#type = 1.买家登录,type=2卖家登录,type=3.安卓用户登录,type=4苹果用户登录
#成功返回1，失败返回0
def login_sel(username, password, type):
    with open("sel_info.txt","r",encoding="utf-8") as sel_info:
        for line in sel_info:
            _line = line.strip().split(",")
            if username == _line[0]:
                if password == _line[1]:
                    print(str_login_ok %(username))
                    return "1"
                else:
                    print(str_login_fail)
                    return "0"
        print(str_user_not_exist)
        return "0"

#展示商品信息 返回商品总个数
def show_item():
    with open("shoppingmall_list.txt","r",encoding="utf-8") as item_list:
        count = 0
        for line in item_list:
            count += 1
            _line = line.strip().split(",")
            print(count,".",_line[0],_line[1])
        return count

#修改文件 type=1修改 type=2删除
def edit_item(type,num,item,price):
    with open("shoppingmall_list.txt", "r", encoding="utf-8") as item_list:
        with open("shoppingmall_list.bak", "w", encoding="utf-8") as new_file:
            count = 0
            for line in item_list:
                count += 1
                _line = line.strip().split(",")
                if num == str(count):
                    if type == 1:
                        line = item + "," + price + "\n"
                    elif type == 2:
                        line = ""
                new_file.write(line)
                new_file.flush()
    os.replace("shoppingmall_list.bak","shoppingmall_list.txt")

while switch_main:
    choise_system = input("您要登录哪个系统：\n1.买家系统\n2.卖家系统")
    if choise_system == "1":
       username = input(str_input_username)
       password = input(str_input_password)
       # 执行登录方法,成功返回1,balance
       login_result = login_cus(username, password, choise_system)
       if login_result[0] == "1":
           balance = int(login_result[1])
           while switch_buy_item:
               print("您的余额为:%d" %balance)
               total = show_item()
               item_num = input("请输入您要购买的商品编号:")
               if item_num.isdigit() and int(item_num) <= total:
                   with open("shoppingmall_list.txt","r",encoding="utf-8") as item_list:
                       count = 0
                       for line in item_list:
                           count += 1
                           if count == int(item_num):
                               _line = line.strip().split(",")
                               if balance-int(_line[1])>=0:
                                   balance = balance-int(_line[1])
                                   print("购买成功！")
                                   #TODO cus_info 修改余额
                                   # modify_balance()
                                   #TODO shopping_list 更新购买记录
                                   # modify_shopping_list()
                               else:
                                   print("余额不足，请充值后重试！")
               else:
                   print(str_wrong_msg)
    elif choise_system == "2":
        username = input(str_input_username)
        password = input(str_input_password)
        login_result = login_sel(username,password,choise_system)
        if login_result[0] == "1":
            while switch_item:
                print("商品列表如下".center(50,"*"))
                show_item()
                ipt_order = input(str_item_order)
                order = ipt_order.split(",")
                if order[0] == "add" and len(order)==3:
                    with open("shoppingmall_list.txt","a+",encoding="utf-8") as item_list:
                        item_list.write(order[1]+","+order[2])
                        print("商品添加成功",order[1],order[2])
                elif order[0] == "edit" and len(order)==4:
                    edit_item(1,order[1],order[2],order[3])
                    print("修改成功！")
                elif order[0] == "del" and len(order)==2:
                    edit_item(2,order[1],"","")
                    print("删除成功！")
                else:
                    print(str_wrong_msg)

    else:
        print(str_wrong_msg)

