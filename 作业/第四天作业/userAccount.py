#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 2:22 PM
# @Author  : zhangjiang
# @Site    : 
# @File    : userAccount.py
# @Software: PyCharm

import loginAndAuthorze as loginM

loginInfo = []

@loginM.login_deco
@loginM.run_time
def transferccounts():
    '''
    转账给指定用户
    :return:
    '''
    loginInfo = loginM.login_info
    flag = True
    #输出当前的账户余额
    tempSalary = loginM.getUserMoney(loginInfo[0])
    print("\033[31m当前用户 %s ,信用额度 %s,可转账 %s\033[0m" %(loginInfo[0],tempSalary,tempSalary))
    while flag:
        account = input("请输入转账账户:>>>").strip().lower()
        #先判断是否是自己
        if account == loginInfo[0]:
            print("\033[31m不能给自己转账\033[0m")
            continue
        users = loginM.getUseraccount()
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
                            users = loginM.getUseraccount()
                            #修改两个人的余额
                            for user in users[:]:
                                if user["account"] == account:
                                    users.remove(user)
                                    user["salary"] = user["salary"] + money
                                    users.append(user)
                                    loginM.changAllAccount(users)
                                if user["account"] == loginInfo[0]:
                                    users.remove(user)
                                    user["salary"] = user["salary"] - money
                                    users.append(user)
                                    loginM.changAllAccount(users)
                            print("\033[31m汇款成功,您当前余额%s,请查看当前余额\033[0m" %(user["salary"]))
                            flag = False
                        else:
                            #取消返回上一级操作
                            flag = False
                else:
                    print("\033[31m骚年金额不足，赶紧充值吧\033[0m")
                    flag = False
                    break
            else:
                print("\033[31m转账金额输入不合法\033[0m")
                break
        else:
            print("\033[31m账号不存在请重新输入\033[0m")


@loginM.login_deco
@loginM.run_time
def withdrawUserMoneyToUser():
    """
    提现实现
    :return:
    """
    loginInfo = loginM.login_info
    flag = True
    # 输出当前的账户余额
    tempSalary = loginM.getUserMoney(loginInfo[0])
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
                        users = loginM.getUseraccount()
                        # 修改余额
                        for user in users[:]:
                            if user["account"] == loginInfo[0]:
                                users.remove(user)
                                user["salary"] = tempSalary - (1+0.05)*withdrawMoney
                                users.append(user)
                                loginM.changAllAccount(users)
                        print("\033[31m提现%s成功,手续费%s,当前账户余额%s,请注意查收\033[0m" %(withdrawMoney,withdrawMoney*0.05,user["salary"]))
                        flag = False
                    else:
                        # 取消返回上一级操作
                        flag = False
        else:
            print("\033[31m提现金额输入不合法\033[0m")
            continue

       
@loginM.login_deco
@loginM.run_time
def repaymentMyBalance():
    '''
    还款操作
    :return:
    '''
    loginInfo = loginM.login_info
    #查看当前账户余额
    money = loginM.getUserMoney(loginInfo[0])
    if money > 0:
        print("\033[31m当前账户余额充足，没有还款信息,👏👏👏土豪尽管花👏👏👏\033[0m")
    else:
        print("\033[31m尊敬的用户 %s 您已欠费 %s，请充值\033[0m" %(loginInfo[0],money))
        flag = True
        while flag:
            inputMoney = input("请输入还款金额:>>>").strip().lower()
            if inputMoney.isdigit():
                while flag:
                    confirm = input("确定要还款吗？(y/n)").strip().lower()
                    if confirm not in ['y', 'n']: continue
                    # 修改账号余额，开始还款
                    if confirm == "y":
                        users = loginM.getUseraccount()
                        for user in users[:]:
                            if user["account"] == loginInfo[0]:
                                users.remove(user)
                                user["salary"] += float(inputMoney)
                                users.append(user)
                                loginM.changAllAccount(users)
                        print("\033[31m还款成功，当前余额%s\033[0m" %(user["salary"]))
                        flag = False
                    else:
                        # 取消返回上一级操作
                        flag = False

            else:
                print("\033[31m金额输入不合法\033[0m")

if __name__ == "__main__":
    transferccounts()