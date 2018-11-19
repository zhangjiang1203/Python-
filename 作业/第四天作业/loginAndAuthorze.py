#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 1:22 PM
# @Author  : zhangjiang
# @Site    : 
# @File    : loginAndAuthorze.py
# @Software: PyCharm
# 装饰器的__内置方法__
from functools import wraps
import os
import time
'''
编写登录装饰器和时间统计装饰器
'''
#用户的登录信息
login_info = []
file_name = 'account.txt'


def login_deco(func):
    '''
    登录的装饰器
    :param func:
    :return:
    '''
    @wraps(func)
    def wrapper(*args,**kwargs):
        # 执行登录代码
        #执行函数并返回值
        global login_info
        if len(login_info) > 0:
            res = func(*args,**kwargs)
            return res
        else:
            flag = True
            while flag:
                # 用户是否存在
                users = getUseraccount()
                isexist = False
                account = input('请输入您的账号:').strip()
                for user in users[:]:
                    if account in user.values():
                        isexist = True
                        flag = int(user['loginCount'])
                        if flag == 3:
                            print('\033[31m您登录密码输入错误次数过多，账号已被锁定\033[0m')
                            flag = False
                            break
                        # 拿到对应的password和count值
                        psw = input("请输入您的密码:").strip()
                        if psw == user['password']:
                            print('\033[32m登录成功\033[0m')
                            # 重置用户登录次数
                            users.remove(user)
                            user['loginCount'] = 0
                            users.append(user)
                            changAllAccount(users)
                            print("执行%s " % (func.__name__))
                            login_info = [account, user["salary"], user['password']]
                            res = func(*args, **kwargs)
                            flag = False
                            break
                        else:
                            flag += 1
                            # 修改用户信息
                            users.remove(user)
                            user['loginCount'] = flag
                            users.append(user)
                            changAllAccount(users)
                            if flag == 3:
                                print('\033[31m密码输入错误3次,账号已被锁定\033[0m')
                                flag = False
                                break
                            else:
                                print('\033[31m密码输入错误%s次,请重试\033[0m' % flag)
                                break
                if not isexist:
                    print('\033[31m用户不存在，请重试\033[0m')
                    while flag:
                        confirm = input("是否要注册账号？(y/n)").strip().lower()
                        if confirm not in ['y', 'n']: continue
                        # 开始注册账号
                        if confirm == "y":
                            register = registerAccount()
                            #注册成功之后开始调用函数
                            if register:
                                res = func(*args, **kwargs)
                                flag = False
                        else:
                            flag = False

                if len(login_info) > 0:
                    return res
    return wrapper

def run_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        end = time.time()
        print("\033[35m函数 %s 执行时间为 %s\033[0m" %(func.__name__, (end - start)))
        return res

    return wrapper

@run_time
def getUseraccount():
    '''
    获取所有用户的存储信息
    :return:
    '''
    #文件是否存在
    if os.path.isfile(file_name):
        with open(file_name, 'r+') as file_object:
            contents = file_object.readlines()
            users = []
            for line in contents:
                templine = line.strip()
                if not len(templine) or line.startswith('#'):
                    continue
                #字符串转字典
                users.append(eval(templine));
        return users
    else:
        with open(file_name, 'a+') as object:
            users = [{'account': 'zhang', 'password': '123456', 'loginCount': 1,'salary':15000},
                     {'account': 'wang', 'password': '123456', 'loginCount': 0,'salary':17000},
                     {'account': 'guo', 'password': '123456', 'loginCount': 1,'salary':16000},
                     {'account': 'xiang', 'password': '123456', 'loginCount': 0,'salary':19000}]
            for value in users:
                account = str(value)
                object.write(account + '\n')
        return users

#存储修改用户的群组
@run_time
def changAllAccount(account):
    '''
    修改存储所有的用户信息
    :param account:
    :return:
    '''
    with open(file_name, 'w+') as file_object:
        for value in account:
            user = str(value)
            file_object.write(user + '\n')

@run_time
def getUserMoney(account):
    """
    获取用户的信用额度
    :param account:
    :return:
    """
    users = getUseraccount()
    for user in users:
        if user["account"] == account:
            return user["salary"]


@run_time
def registerAccount():
    '''
    用户注册
    :return:
    '''
    # 获取所有的用户
    global login_info
    flag = True
    while flag:
        account = input("请输入账号>>>").strip()
        users = getUseraccount()
        isexist = False
        for user in users:
            if account in user.values():
                isexist = True
                print("\033[31m该账号已存在，请重新输入\033[0m")
                break
        if isexist: continue
        while flag:
            password = input("请输入密码>>>").strip()
            confirm = input("请再次输入密码>>>").strip()
            if password != confirm:
                print("\033[31m两次输入密码不一致,请重新输入\033[0m")
            else:
                # 用户输入个人薪资
                while flag:
                    salary = input("请输入薪资>>>").strip()
                    if salary.isdigit():
                        # 保存用户信息
                        temp = {'account': account, 'salary': float(salary), 'loginCount': 0, 'password': confirm}
                        login_info = [account, float(salary), confirm]
                        users.append(temp)
                        changAllAccount(users)
                        flag = False
                        return True
                    else:
                        print("\033[0m输入有误\033[0m")