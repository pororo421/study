   #-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/12 17:34
# @File: menu_qlt.py
# @Software: PyCharm
menu = {
    "湖南省": {
        "长沙市": ["芙蓉区", "天心区", "岳麓区"],
        "张家界市": "",
        "株洲市": ""
    },
    "河北省": {
        "石家庄市": "",
        "唐山市": "",
        "秦皇岛市": "",
        "邯郸市": "",
        "廊坊市": ""
    },
    "吉林省": {
        "长春市": ["南关区", "朝阳区", "绿园区"],
        "四平市": "",
        "延边州": ["延吉市", "珲春市", "图们市"],
        "白山市": ""
    }
}

is_run = True  # 是否终止
second_run = True

while is_run:
    level = 2
    f_count = 1
    print("-----------------查询省会信息系统------------------")
    # 1.运行程序显示省份信息，要求用户输入
    for province in menu:
        print(str(f_count) + "." + province)
        f_count = f_count + 1
    first_menu = input("请输入要查询的省名称:(如需关闭程序请输入q)")
    # 2.如果用户已输入省份查询输入的是否存在
    if first_menu == "q":
        is_run = False
        break
    elif menu.get(first_menu, "") != "" and level == 2:
        while second_run:
            print("----------------------------查询 #" + first_menu + "# 结果----------------------------------------")
            s_count = 1
            third_run = True
            for city in menu[first_menu]:
                print(str(s_count) + "." + city)
                s_count = s_count + 1
            second_menu = input("请输入要查询的城市名称:(1.如需返回上一级请输入#，2.关闭程序请输入q)")

            if second_menu == "#":
                # level = 1
                break
            elif second_menu == "q":
                second_run = False
                is_run = False
                break
            elif menu[first_menu].get(second_menu, "") != "":
                while third_run:
                    print("----------------------------查询 #" + second_menu + "# 结果----------------------------------------")
                    # print(str(menu[first_menu][second_menu]))
                    t_count = 1
                    for area in menu[first_menu][second_menu]:
                        print(str(t_count) + "." + area)
                        t_count = t_count + 1
                    last_input = input("查询完成，1.如需返回上一级请输入#，2.返回主菜单请输入*，3.如需关闭程序请输入q")
                    if last_input == "#":
                        third_run = False
                        continue
                    elif last_input == "*":
                        third_run = False
                        second_run = False
                        break
                    elif last_input == "q":
                        second_run = False
                        is_run = False
                        third_run = False
                        break
                    else:
                        print("输入错误，请重新输入！")
                        # third_run = False
                        continue
            else:
                print("输入的城市信息不存在！(如需返回上一级请输入#)")
    else:
        print("输入的省份信息不存在！")