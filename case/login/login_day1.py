# -*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/9 15:06
# @File: login_day1.py
# @Software: PyCharm
'''
编写登录接口
 输入用户名密码
 认证成功显示欢迎信息
 错误三次后锁定
'''
is_login=True #登录成功时False
while is_login:

    # 输入用户名与密码
    username = input("用户名")
    password = input("密码")
    time_log = 0
    # 打开login_log 文件
    login_log = open("login_log.txt", "r")
    for line in login_log.readlines():
        # 获取文件中第一行的内容并用逗号拆分，分成用户名与登录次数
        name_log = line.split(',')[0]  # 登陆次数文件中的用户名
        time_log = int(line.split(',')[1])  # 登陆次数文件中的次数
        # print("用户名：{name} 次数:{time}".format(name=name_log, time=time_log))
        # 判断输入的用户名是否与获取的用户名一致，判断登录次数是否超过三次，是：提示用户账号已被锁定
        if username == name_log:
            if time_log > 2:
                print("密码输错三次以上，账号已被锁定！")
            break
    if time_log < 3:
        # 打开用户信息文件
        user_info = open("user_info.txt", "r")
        user_is_exist = False  # 用户存在时true，不存在false
        for line in user_info.readlines():
            # 获取文件中第一行的内容并用逗号拆分，分成用户名与登录次数
            name_info = line.split(',')[0]
            pass_info = line.split(',')[1].replace('\n', '')
            # print("用户名：{name} 密码：{pass}".format(name=name_info, pass=pass_info))
            # 1.判断用户名与密码相同，是：认证成功显示欢迎信息
            # 2.用户名相同，密码不相同
            # 3.用户名不存在
            if username == name_info:
                user_is_exist = True
                if password == pass_info:
                    print("欢迎{name}".format(name=username), "登录")
                    is_login = False
                    break
                else:
                    print("用户名或密码错误")
                    log = open("login_log.txt", "r")
                    err_name_is_exist = False #用户不在文件时True，否则Flase
                    log_file = "" # 用来保存登录日志信息
                    for line in log.readlines():
                        name_log = line.split(',')[0]
                        time_log = int(line.split(',')[1])
                        #如果存在用户名，修改错误次数，若不存在，在末尾添加用户名与次数
                        if username == name_log:
                            err_name_is_exist = True
                            err_log = str(time_log + 1)
                            line = name_log + ","+err_log+"\n"
                            # open("login_log.txt", 'w').write(err_log)
                        log_file = log_file + line
                    if err_name_is_exist is False:
                       # print("文件中不存在此用户！")
                        log_file = log_file+ "\n"+username+",1"
                    open("login_log.txt", 'w').write(log_file)

        if user_is_exist is False:
            print("用户名不存在")