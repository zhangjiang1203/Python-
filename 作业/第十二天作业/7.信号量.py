#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-28 10:38
# @Author  : zhangjiang
# @Site    : 
# @File    : 7.信号量.py
# @Software: PyCharm

from threading import Thread,Semaphore,current_thread
import time,random

# 同一时间的信号量，同时只能执行五个
sm = Semaphore(5)

def task():
    # mutex.acquire()
    # mutex.release()
    # with操作相当于上面的两步操作，自己添加锁和解锁操作
    with sm:
        print("%s 正在上厕所" %current_thread().name)
        time.sleep(random.randint(1,4))

if __name__ == '__main__':
    for i in range(20):
        t = Thread(target=task)
        t.start()