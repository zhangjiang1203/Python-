#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-14 17:34
# @Author  : zhangjiang
# @Site    : 
# @File    : 04-守护进程.py
# @Software: PyCharm

from multiprocessing import Process
import time

def foo():
    print(123)
    time.sleep(1)
    print('end123')

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == "__main__":
    p1 = Process(target=foo)
    p2 = Process(target=bar)
    # 进程守护 守护的是主线程 主线程执行完毕之后 子线程就不会执行 p1就不会执行
    p1.daemon = True
    p1.start()
    p2.start()
    print("main---")

