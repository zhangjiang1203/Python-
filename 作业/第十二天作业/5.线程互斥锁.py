#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-28 09:40
# @Author  : zhangjiang
# @Site    : 
# @File    : 5.线程互斥锁.py
# @Software: PyCharm


from threading import Thread,Lock
import time

x = 100

# def task():
#     global x
#     temp = x
#     time.sleep(0.1) #延迟执行之后，x最后输出的值都是99，
#     x = temp - 1
#     print(x)
#
# if __name__ == "__main__":
#     t_list = []
#     for i in range(100):
#         t = Thread(target=task)
#         t_list.append(t)
#         t.start()
#
#     for t in t_list:
#         t.join()


# 定义一个锁
mutex = Lock()
def task():
    #加锁之后程序变成串行执行
    global x
    mutex.acquire() #加锁
    temp = x
    time.sleep(0.1) #执行耗时操作的时候必须要加锁，
    x = temp - 1
    mutex.release() #解除锁
    print(x)

if __name__ == "__main__":
    t_list = []
    for i in range(100):
        t = Thread(target=task)
        t_list.append(t)
        t.start()

    for t in t_list:
        t.join()


