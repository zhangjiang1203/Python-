#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ATM.py
# @Author: zhangjiang
# @Date  : 2018/11/15
# @Desc  :
import os
#编辑用户
file_name = 'account.txt'
#保存用户信息 账号 余额 密码
loginInfo = []
shopCar = {}
shopFlag = True

product_list = [['Iphone7',5800],
                ['Coffee',30],
                ['疙瘩汤',10],
                ['Python Book',99],
                ['Bike',199],
                ['ViVo X9',2499]]

def login():
    flag = True
    global loginInfo
    while flag:
        # 用户是否存在
        users = getUseraccount()
        # for user in users:
        #     print(user)
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
                #拿到对应的password和count值
                psw = input("请输入您的密码:").strip()
                if psw == user['password']:
                    print('\033[32m登录成功\033[0m')
                    #重置用户登录次数
                    users.remove(user)
                    user['loginCount'] = 0
                    users.append(user)
                    changAllAccount(users)

                    loginInfo = [account,user["salary"],user['password']]
                    flag = False
                    break
                else:
                    flag+=1
                    #修改用户信息
                    users.remove(user)
                    user['loginCount'] = flag
                    users.append(user)
                    changAllAccount(users)
                    if flag == 3:
                        print('\033[31m密码输入错误3次,账号已被锁定\033[0m')
                        flag = False
                        break
                    else:
                        print('\033[31m密码输入错误%s次,请重试\033[0m' %flag)
                        break;
        if not isexist:
            print('\033[31m用户不存在，请重试\033[0m')


def getUseraccount():
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
def changAllAccount(account):
    with open(file_name, 'w+') as file_object:
        for value in account:
            user = str(value)
            file_object.write(user + '\n')

#注册
def registerAccount():
    '''
    用户注册
    :return:
    '''
    # 获取所有的用户
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
                        users.append(temp)
                        changAllAccount(users)
                        flag = False
                    else:
                        print("\033[0m输入有误\033[0m")


#购物
def shoppingAction():
    global shopFlag
    global shopCar
    if len(loginInfo) == 0:
        print("\033[31m还没有登录，请先登录\033[0m")
        login()
    else:
        user_name = loginInfo[0]
        user_balance = loginInfo[1]
        print("\033[32m尊敬的用户 %s 你的余额为%s,预祝你购物愉快\033[0m" % (user_name, user_balance))

        while shopFlag:
            for index, shop in enumerate(product_list):
                print(index, shop)
            choice = input("请输入商品编号进行购买，输入q退出:>>>").strip()
            if choice.isdigit():
                choice = int(choice)
                if choice < 0 or choice >= len(product_list): continue
                # 添加商品，展示用户余额信息。若是余额不够就提示用户金钱不足
                goods = product_list[choice]
                # 修改金额
                good_price = goods[1]
                good_name = goods[0]
                if user_balance >= good_price:
                    if good_name in shopCar:
                        # 之前已经添加到购物车
                        shopCar[good_name]["count"] += 1
                    else:
                        shopCar[good_name] = {"price": good_price, "count": 1}
                    user_balance -= goods[1]
                    # 更新用户余额
                    loginInfo[1] = user_balance
                    # 输出购买数据
                    print("\033[34m%s已添加到购物车，剩余金额%s\033[0m" % (good_name, str(user_balance)))
                else:
                    print("\033[31m余额不足，还差%s元，请充值🤣🤣🤣🤣\033[0m" % (good_price-user_balance))
            else:
                if choice.lower() == "q":
                    if len(shopCar) == 0: shopFlag = False
                    print("\033[31m已购买商品\033[0m".center(80, "*"))
                    print("\033[31mid          商品           数量          单价          总价\033[0m")
                    total = 0
                    for i, key in enumerate(shopCar):
                        print("\033[31m%s%18s%10s%13s%13s\033[0m" % (i, key, shopCar[key]["count"],
                                                                     shopCar[key]["price"],
                                                                     shopCar[key]["price"] * shopCar[key]["count"]))
                        total += shopCar[key]["price"] * shopCar[key]["count"]

                    print("\033[31mend\033[0m".center(80, "*"))
                    while shopFlag:
                        confirm = input("确定要购买吗？(y/n)").strip().lower()
                        if confirm not in ['y', 'n']: continue
                        # 修改账号余额，清空购物车
                        if confirm == "y":
                            users = getUseraccount()
                            for user in users[:]:
                                if user["account"] == user_name:
                                    print("\033[31m此次购物总花费: %s  你的余额为: %s\033[0m" % (total, user_balance))
                                    users.remove(user)
                                    user["salary"] = user_balance
                                    users.append(user)
                                    changAllAccount(users)
                                    shopFlag = False
                                    shopCar = {}
                                    continue
                        else:
                            # 清空购物车
                            shopCar = {}
                            shopFlag = False
                else:
                    print("\033[31m请输入商品编号\033[0m")

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

def transferccounts():
    '''
    转账给指定用户
    :return:
    '''
    flag = True
    #输出当前的账户余额
    tempSalary = getUserMoney(loginInfo[0])
    print("\033[31m当前用户 %s ,信用额度 %s,可转账 %s\033[0m" %(loginInfo[0],tempSalary,tempSalary))
    while flag:
        account = input("请输入转账账户:>>>").strip().lower()
        #先判断是否是自己
        if account == loginInfo[0]:
            print("\033[31m不能给自己转账\033[0m")
            continue
        users = getUseraccount()
        isexist = False
        for user in users[:]:
            if account in user.values():
                isexist = True
        if isexist:
            money = input("请输入转账金额:>>>").strip().lower()
            if money.isdigit():
                #判断金额是否充足
                money = float(money)
                if tempSalary >= money:
                    while flag:
                        confirm = input("确定要转账吗？(y/n)").strip().lower()
                        if confirm not in ['y', 'n']: continue
                        # 修改账号余额，开始转账
                        if confirm == "y":
                            users = getUseraccount()
                            #修改两个人的余额
                            for user in users[:]:
                                if user["account"] == account:
                                    users.remove(user)
                                    user["salary"] = user["salary"] + money
                                    users.append(user)
                                    changAllAccount(users)
                                if user["account"] == loginInfo[0]:
                                    users.remove(user)
                                    user["salary"] = user["salary"] - money
                                    users.append(user)
                                    changAllAccount(users)
                            print("\033[31m汇款成功,请注意查收\033[0m")
                            flag = False
                        else:
                            #取消返回上一级操作
                            flag = False
                else:
                    print("\033[31m骚年金额不足，赶紧充值吧\033[0m")
            else:
                print("\033[31m转账金额输入不合法\033[0m")
                break
        else:
            print("\033[31m账号不存在请重新输入\033[0m")


def withdrawUserMoneyToUser():
    """
    提现实现
    :return:
    """
    flag = True
    # 输出当前的账户余额
    tempSalary = getUserMoney(loginInfo[0])
    print("\033[31m当前用户 %s ,当前余额 %s,本次提现要扣除5%%的手续费\033[0m" % (loginInfo[0], tempSalary))
    while flag:
        withdrawMoney = input("请输入提现的金额:>>>").strip().lower()
        if withdrawMoney.isdigit():
            withdrawMoney = float(withdrawMoney)
            if withdrawMoney > (tempSalary*0.95):
                print("\033[31m 大哥钱不够，赶紧充值吧 😂😂😂😂\033[0m")
                flag = False
            else:
                #开始提现，修改用户数据
                print("\033[31m本次提现要扣除5%%的手续费，共计%s\033[0m" %(withdrawMoney*0.05))
                while flag:
                    confirm = input("确定要提现吗？(y/n)").strip().lower()
                    if confirm not in ['y', 'n']: continue
                    # 修改账号余额，开始转账
                    if confirm == "y":
                        users = getUseraccount()
                        # 修改两个人的余额
                        for user in users[:]:
                            if user["account"] == loginInfo[0]:
                                users.remove(user)
                                user["salary"] = tempSalary - (1+0.05)*withdrawMoney
                                users.append(user)
                                changAllAccount(users)
                        print("\033[31m提现%s成功,手续费%s,当前账户余额%s,请注意查收\033[0m" %(withdrawMoney,withdrawMoney*0.05,user["salary"]))
                        flag = False
                    else:
                        # 取消返回上一级操作
                        flag = False
        else:
            print("\033[31m提现金额输入不合法\033[0m")
            continue

if __name__ == "__main__":

    while shopFlag:
        if len(loginInfo) > 0:
            print("""
                3.购物
                4.转账
                5.提现
                6.还款
                7.退出
                """)
        else:
            print("""
                1.登录
                2.注册
                """)
        choice = input(" 请选择:>>>").strip()
        if choice.isdigit() :
            if len(loginInfo) == 0:
                if choice == "1":
                    login()
                elif choice == "2":
                    registerAccount()
                else:
                    print("\033[31m输入不合法，请重新输入\033[0m")
            else:
                if choice == "3":
                    shoppingAction()
                elif choice == "4":
                    transferccounts()
                elif choice == "5":
                    withdrawUserMoneyToUser()
                elif choice == "6":
                    print("")
                elif choice == "7":
                    loginInfo = []
                    break
                else:
                    print("\033[31m输入不合法，请重新输入\033[0m")
        else:
            print("\033[31m请输入数字\033[0m")