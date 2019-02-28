#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-27 17:17
# @Author  : zhangjiang
# @Site    : 
# @File    : 3.同一个进程下线程共享数据.py
# @Software: PyCharm


'''
同一个进程之间的数据在线程之间是共享的
'''

from threading import Thread

x = 100
def task():
    global x
    x = 1000

if __name__ == "__main__":
    t = Thread(target=task)
    t.start()
    print(x)
    t.is_alive()#线程是否存活
    t.join()#等待子线程执行完毕
    t.daemon = True #守护线程守护的就是本进程内的所有非守护的进程都死掉了才跟着死