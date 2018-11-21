#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 11:26 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : 有参装饰器.py
# @Software: PyCharm
from functools import wraps
import time
import os

def auth(driver):
    def auth2(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            #拿到driver的值进行下一步的操作
            start = time.time()
            res = func(*args,**kwargs)
            end = time.time()
            print("参数是 %s 函数 %s 执行时间是 %s" %( driver,func.__name__,end-start))
            return res
        return wrapper
    return auth2


@auth("你好，世界")
def foo(name):
    time.sleep(1)
    print(name)



def actionRecord(func):

    def wrapper(*args,**kwargs):
        #获取时间，保存文件
        res = func(*args,**kwargs)
        with open('recordLog.txt',"r+",encoding='utf-8') as read_f, open('.recordLog.txt.swap', 'w+',encoding="utf-8") as write_f:
            for line in read_f:
                line = line.replace('alex', 'SB')
                write_f.write(line)
            timeStr = time.strftime("%Y-%m-%d %X ")
            write_f.write("时间：" + timeStr + "函数名：" + func.__name__ + " run \n")
        os.remove('recordLog.txt')
        os.rename('.recordLog.txt.swap', 'recordLog.txt')

        return res
    return wrapper

@actionRecord
def recordMyAction(file):
    print("开始操作---%s" %file)

@actionRecord
def myNameAction(name):
    print("我们的过去===%s" %name)

if __name__ == "__main__":
    recordMyAction("你好")
    myNameAction("哈哈哈")



'''
有参装饰器就是在无惨装饰器上再加一层函数嵌套，返回的参数和函数调用都是和无参装饰器一样的
多个装饰器可以一起使用，使用装饰器的语法糖每一行单独写一个装饰器，一直到函数调用
'''