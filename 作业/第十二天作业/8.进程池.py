#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-28 10:55
# @Author  : zhangjiang
# @Site    : 
# @File    : 8.进程池.py
# @Software: PyCharm

import os
import time
from multiprocessing import Pool ,Process
from threading import current_thread

def task(i):
    i += 1
    # print("%s 当前线程 %s" %(i,current_thread().name))


if __name__ == '__main__':
    #cpu个数
    # print(os.cpu_count())
    #定义进程池
    start = time.time()
    p = Pool(10)  #实例化7个进程,每次执行7个进程
    p.map(task,range(2000)) #进程中里面的start,p.map就是异步操作
    p.close()  #不能再往里面提交任务
    p.join()   #等待子进程执行完毕
    end = time.time()
    print("执行时间===%s" %(end - start))

    #原生进 程
    start = time.time()
    p_l = []
    for i in range(2000):
        p = Process(target=task,args=(i,))
        p_l.append(p)
        p.start()

    for p in p_l:
        p.join()
    end = time.time()
    print("原生执行的时间:%s" %(end - start))