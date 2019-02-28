#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-27 17:08
# @Author  : zhangjiang
# @Site    : 
# @File    : 2.进程线程速度的对比.py
# @Software: PyCharm

import time
from multiprocessing import Process
from threading import Thread


'''--------------------- 函数的开启方式---------------------'''
def processtask(arg):
    print("%s is runing" %arg)
    time.sleep(1)
    print("%s is done" %arg)


def threadtask(arg):
    print("%s is runing" % arg)
    time.sleep(1)
    print("%s is done" % arg)


if __name__ == '__main__':
    t = Thread(target=processtask, args=('子线程',))
    p = Process(target=processtask,args=('子进程',))

    t.start() #开启的瞬间就执行
    p.start()
    print('主线程2')