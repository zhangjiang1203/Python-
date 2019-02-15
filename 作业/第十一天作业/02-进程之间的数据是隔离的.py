#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-13 17:46
# @Author  : zhangjiang
# @Site    : 
# @File    : 02-进程之间的数据是隔离的.py
# @Software: PyCharm
import time
from multiprocessing import Process

x = 100

def task(x,t):
    print("%s is running" %x)
    time.sleep(t)
    print("%s is done" %x)


if __name__ == "__main__":
    # p = Process(target=task)
    # p.start()
    # time.sleep(3)
    # p.join()  #等待子进程执行完毕
    # print('x的值是多少===%s' %x)
    # # x的值保持不变，子进程修改不了主进程中的数据
    #开启多个进程
    p1 = Process(target=task,args=('子进程%s' %1,1))
    p2 = Process(target=task, args=('子进程%s' %2, 2))
    p3 = Process(target=task, args=('子进程%s' %3, 3))

    begin = time.time()
    # p1.start()
    # p2.start()
    # p3.start()
    # #不设置join的时候主线程之间就执行不会等待，添加join之后 主线程会等待执行
    # #这样设置之后 进程执行3秒之后就结束了
    # # 这是并行执行，每个都可能执行
    # p1.join()
    # p2.join()
    # p3.join()
    # end = time.time()
    # print('主进程')
    # print('执行时间为==%s' %(end-begin))

    # 进程执行顺序的设置,这时候程序执行的时间都不一样了
    # 下面这种是串行执行 ，只有执行完一个之后下一个才开始执行
    p1.start()
    p1.join()

    p2.start()
    p2.join()

    p3.start()
    p3.join()
    end = time.time()
    print('主进程')
    print('执行时间为==%s' % (end - begin))