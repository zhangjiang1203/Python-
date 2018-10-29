#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最新作业练习.py
# @Author: zhangjiang
# @Date  : 2018/10/29
# @Desc  :

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 1-第一天作业.py
# @Author: zhangjiang
# @Date  : 2018/10/29
# @Desc  : 第一次作业

loginStr = "|".join(["你好","jiushi","12"])
print(loginStr)

def login_test():
    flag = True
    while flag:
        account = input("请输入用户名:")
        password = input("请输入密码:")
        count = 0
        if account == "zhangsan" and password == "123456":
            print("登录成功")
            tempArr = [account,password,count]
            loginStr = "|".join(tempArr)
            while flag:
                command = input("请输入其他命令，输入Q或q退出:")
                if command == "Q" or command == "q":
                    flag = False
                    break
        else:
            print("账号或密码错误，请重新输入")


if __name__ == "__main__":
    login_test()

