# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/17 11:45
# @File: test.py
# @Software: PyCharm
str_cmd = '''
操作指南：
删除：d,产品编号 （例：d,2)
添加：a,产品名称,价格（例：a,samsung,1000）
修改：m,序号,产品名称,价格 （例：m,2,sansumg1,999）
请选择指令：
'''
delete = "d"  # 删除操作
add = "a"  # 添加操作
modify = "m"  # 修改操作

with open("shoppingmall_list.txt", "r", encoding="UTF-8") as list:
    for index, product in enumerate(list.readlines()):
        print(index + 1, ".", product)

_product = input(str_cmd)
new_file = ""
with open("shoppingmall_list.txt", "r", encoding="UTF-8") as del_list:
    # for index, product in enumerate(del_list.readlines()):
    cmd = _product.split(",")
    if cmd[0] == delete and len(cmd) == 2:
        for index, product in enumerate(del_list.readlines()):
            if cmd[1] == str(index + 1):  # 判断商家选择删除的产品是否在产品列表里 是：删除该产品
                new_file = new_file + ""  # 将要删除的产品赋予空值
                continue
            new_file = new_file + product
    elif cmd[0] == add and len(cmd) == 3:
        with open("shoppingmall_list.txt", "a+", encoding="utf-8") as add_list:
            add_list.write("\n" + cmd[1] + "," + cmd[2])
    elif cmd[0] == modify and len(cmd) == 4:
        # with open("shoppingmall_list.txt","r",encoding="utf-8") as mod_list:
        for index, product in enumerate(del_list.readlines()):
            if cmd[1] == str(index + 1):
                new_file = new_file + cmd[2] + "," + cmd[3]+"\n"
                continue
            new_file = new_file + product
    else:
        print("您输入的指令有误！")
if cmd[0] == delete or cmd[0]==modify:  # 判断用户输入的指令是否为删除
    with open("shoppingmall_list.txt", "w", encoding="UTF-8") as new_list:
        print(new_file)
        new_list.write(new_file)




'''
                    while sel_choice:
                        sel_ope_choice = input(
                            "1.add 2.delete 3.modify\nWhich operation do you want to choice? ")  # sel_ope_choice 商家选择要进行的操作
                        if sel_ope_choice == "1":
                            sel_pro_add = input("please input add information:")  # sel_pro_add 商家添加的内容
                            print("您添加的内容为：", sel_pro_add)
                            # with open("shoppingmall_list.txt")
                        elif sel_ope_choice == "2":
                            sel_pro_del = input("which product do you want to delete?")  # sel_pro_del  商家要删除的产品
                            print("您要删除的产品为：", sel_pro_del)

                                # print(sel_pro_del,"与文件产品匹配成功")

                        elif sel_ope_choice == "3":
                            sel_pro_mod_cho = input("which product do you want to modify?")  # sel_pro_mod_cho 商家要修改的产品
                            print("您要修改的产品为：", sel_pro_mod_cho)
                            sel_pro_mod = input("please input modify information:")  # sel_pro_mod 商家要修改的内容
                            print("您要修改的内容为：", sel_pro_mod)
                            '''
