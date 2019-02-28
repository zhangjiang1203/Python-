#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-28 10:13
# @Author  : zhangjiang
# @Site    : 
# @File    : 6.死锁和递归锁.py
# @Software: PyCharm

from threading import Thread,Lock,RLock
import time
# mutexA = Lock()
# mutexB = Lock()
#
# class MyThread(Thread):
#     def run(self):
#         self.f1()
#         self.f2()
#
#     def f1(self):
#         mutexA.acquire()
#         print("%s 拿到A锁" %self.name)  #拿到A锁
#         mutexB.acquire()
#         print("%s 拿到B锁" %self.name)  #拿到B锁
#         mutexB.release()
#         mutexA.release()
#
#     def f2(self):
#         mutexB.acquire()
#         print("%s 拿到B锁" %self.name)  #这边也拿到B锁
#         time.sleep(1)
#         mutexA.acquire()               #上面的A锁没有释放，一直等待，再次执行的时候f1中的函数等待A锁和B锁的释放 这样一直等待下去
#         print("%s 拿到A锁" %self.name)
#         mutexA.release()
#         mutexB.release()
#
# if __name__ == "__main__":
#     for i in range(10):
#         t = MyThread()
#         t.start()


'''
解决办法：使用递归锁，一直执行,递归锁可以连续的acquire
'''
obj = RLock()
mutexA = obj
mutexB = obj

class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print("%s 拿到A锁" %self.name)  #拿到A锁
        mutexB.acquire()
        print("%s 拿到B锁" %self.name)  #拿到B锁
        mutexB.release()
        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print("%s 拿到B锁" %self.name)  #这边也拿到B锁
        time.sleep(1)
        mutexA.acquire()               #上面的A锁没有释放，一直等待，再次执行的时候f1中的函数等待A锁和B锁的释放 这样一直等待下去
        print("%s 拿到A锁" %self.name)
        mutexA.release()
        mutexB.release()

if __name__ == "__main__":
    for i in range(10):
        t = MyThread()
        t.start()


