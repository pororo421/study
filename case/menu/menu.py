# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/11 10:04
# @File: menu.py
# @Software: PyCharm

china_city = {
    "吉林省": {
        "长春市": ['南关区', '宽城区', '朝阳区'],
        "吉林市": ['昌邑区', '船营区', '龙潭区'],
        "通化市": ['东昌区', '二道江区']
    },
    "辽宁省": {
        "沈阳市": ['和平区', '沈河区', '皇姑区'],
        "盘锦市": ['盘山县', '大洼县', '双台子区'],
        "抚顺市": ['顺城区', '新抚区', ' 望花区']
    },
    "黑龙江省": {
        "哈尔滨市": ['道里区', '南岗区', '道外区'],
        "佳木斯市": ['前进区', '向阳区', '东风区'],
        "鸡西市": ['鸡冠区', '城子河区', '恒山区']
    }
}
exit_menu = "0"
return_menu = "1"
main_menu = "2"
is_start = True  # 想要停止是False
is_city = True  # 想要停止是False
is_area = True

while is_start:
    for key in china_city:
        print(key)
    province = input("请出入您要选择的省份（退出请输入0）：")

    if province == exit_menu:
        break
    elif china_city.get(province, "") == "":
        print("您输入的省份不存在！")
    else:
        # print("您输入的是：" + str(china_city[province]))
        is_city = True
        while is_city:
            for city in china_city[province]:
                print(city)
                # is_start = False
            input_city = input("请输入您要选择的城市（退出请输入0，返回请输入1）：")
            if input_city == exit_menu:
                break
            elif input_city == return_menu:
                is_city = False
                break
            elif china_city[province].get(input_city, "") == "":
                print("您输入的城市不存在！")
            else:
                is_area = True
                while is_area:
                    for area in china_city[province][input_city]:
                        print(area)
                    input_area = input("退出请输入0，返回上一级请输入1，返回主菜单请输入2：")
                    if input_area == exit_menu:
                        is_area = False
                        is_city = False
                        is_start = False
                        break
                    elif input_area == return_menu:
                        is_area = False
                        break
                    elif input_area == main_menu:
                        is_area = False
                        is_city = False
                        break
                    else:
                        print("您输入有误，请重新输入！")
                        continue
