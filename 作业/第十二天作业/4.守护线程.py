#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-28 09:17
# @Author  : zhangjiang
# @Site    : 
# @File    : 4.守护线程.py
# @Software: PyCharm
import time
from threading import Thread

def foo():
    print('i am foo')
    time.sleep(3)
    print('foo is done')


def bar():
    print('i am bar')
    time.sleep(1)
    print('bar is done')


if __name__ == "__main__":
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)
    t1.daemon = True
    t1.start()
    t2.start()

    # 非守护线程都执行完了之后，守护的是进程内的其他非守护线程，主线程和其他线程执行完毕之后，守护线程才会执行
    # 生命周期都已经结束掉了，守护线程下面的就不会在执行
    print("------main-----")