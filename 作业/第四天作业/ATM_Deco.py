#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 2:39 PM
# @Author  : zhangjiang
# @Site    : 
# @File    : ATM_Deco.py
# @Software: PyCharm

import loginAndAuthorze as loginM
import Shopping
import userAccount

if __name__ == "__main__":
    actionArr = {"1":Shopping.shoppingAction,
                 "2":userAccount.transferccounts,
                 "3":userAccount.withdrawUserMoneyToUser,
                 "4":userAccount.repaymentMyBalance,
                 "5":loginM.lookRecordInfo}
    while True:
        print("""
            1.购物
            2.转账
            3.提现
            4.还款
            5.查看操作日志
            6.退出
            """)
        loginInfo = loginM.login_info
        choice = input(" 请选择:>>>").strip()
        if choice.isdigit() :
            if choice == "6": break
            if choice in actionArr:
                actionArr[choice]()
            else:
                print("\033[31m输入不合法,请重新输入\033[0m")
        else:
            print("\033[31m请输入数字\033[0m")