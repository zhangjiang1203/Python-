#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-14 16:20
# @Author  : zhangjiang
# @Site    : 
# @File    : 03-进程串行和并行.py
# @Software: PyCharm

from multiprocessing import Process
import time,os

def task(x,t):
    # os.getpid 获取当前进程 os.getppid  获取当前父进程
    print("%s is runing %s " %(x,os.getpid()))
    time.sleep(t)
    print("%s is done" %x)

if __name__ == "__main__":
    p_l = []
    # 创建多个进程 并行执行
    begin = time.time()
    for i in range(10):
        # 进程设置名字和参数
        p = Process(target=task,name='我是进程%s' %i,args=('当前进程%s' %i,1))
        p_l.append(p)
        p.start()
        print('当前的进程的id==%s  name=%s' %(p.pid,p.name))
        # p.join()  #添加在这个地方就是串行执行的 一个执行完了之后才会执行下一个

    for p in p_l:
        p.join()  #添加到这个地方执行 就是并行执行的，随机展示数据

    end = time.time()
    print("执行时间%s" %(end-begin))
