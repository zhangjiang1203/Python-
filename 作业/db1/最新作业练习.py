#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最新作业练习.py
# @Author: zhangjiang
# @Date  : 2018/10/29
# @Desc  :

import os

filePath = "userName.txt"

def login_test():
    flag = True
    while flag:
        account = input("请输入用户名:")
        #判断该用户是否存在
        accounts = []
        users = getUsersInfo()
        for user in users:
            accounts.append(user["account"])
        #判断是否存在该账号
        if account in accounts:
            for user in users:
                if account == user["account"]:
                    logincount = int(user["loginCount"])
                    if logincount >= 3:
                        print("账号已被锁定，请联系管理员")
                        break
                    else:
                        password = input("请输入密码:")
                        if password == user["password"]:
                            print("登录成功")
                            while flag:
                                order = input("请输入其他指令,输入q或Q退出:")
                                if order.lower() == "q":
                                    flag = False
                                    break
                        else:
                            logincount += 1
                            print("密码已输错%d次" % logincount)
                            users.remove(user)
                            # 保存用户数据. 记录
                            user["loginCount"] = str(logincount)
                            users.append(user)
                            saveUserLoginInfo(users)
                            break

        else:
            print("账号不存在，请重新输入")

def getUsersInfo():
    """
    获取所有的用户信息，返回用户账号列表
    :return:
    """
    #判断文件是否存在,存在直接读取，不存在创建文件
    if os.path.isfile(filePath):
        with open(filePath,'r+',encoding='utf-8') as obj:
            all_lines = obj.readlines()
            users = []
            for value in all_lines:
                tempLine = value.strip()
                if not len(tempLine) or tempLine.startswith("#"):
                    continue
                users.append(eval(tempLine))
        return users
    else:
        #文件不存在直接创建一个文件
        with open(filePath,'a+',encoding='utf-8') as obj:
            userInfo = [{"account":"zhangsan", "password": "123456", "loginCount": "0"},
                        {"account": "lisi", "password": "654321", "loginCount": "2"},
                        {"account": "wangwu", "password": "123456", "loginCount": "0"},
                        {"account": "zhaoer", "password": "123456", "loginCount": "1"}]
            for value in userInfo:
                tempUser = str(value)
                obj.write(tempUser + "\n")
        return userInfo

def saveUserLoginInfo(users):
    """
    保存用户数据,重新覆盖之前的文件
    :param account:
    :return:
    """
    with open(filePath,'w+',encoding='utf-8') as obj:
        for user in users:
            obj.write(str(user) + "\n")


if __name__ == "__main__":
    login_test()

