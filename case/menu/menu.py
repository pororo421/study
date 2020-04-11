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

for key in china_city:
    print(key)
province = input("请出入您要选择的省份：")
print("city:", china_city[province])
for city in china_city[province]:
    print(city)
city = input("请输入您要选择的城市：")
print("area:", china_city[province][city])
for area in china_city[province][city]:
    print(area)