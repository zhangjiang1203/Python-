#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-27 16:50
# @Author  : zhangjiang
# @Site    : 
# @File    : 1.线程开启的两种方式.py
# @Software: PyCharm
import time
from multiprocessing import Process
from threading import Thread


'''--------------------- 函数的开启方式---------------------'''
# def task(arg):
#     print("%s is runing" %arg)
#     time.sleep(1)
#     print("%s is done" %arg)
#
#
# if __name__ == '__main__':
#     t = Thread(target=task, args=('子线程',))
#     t.start() #开启的瞬间就执行
#     print('主线程')


# 类的方式开启
class MyThread(Thread):

    def run(self):
        print("hello")


if __name__ == "__main__":
    p =  MyThread()
    p.start()

    print("主")