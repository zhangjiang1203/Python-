#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-15 14:13
# @Author  : zhangjiang
# @Site    : 
# @File    : 05-模拟抢票.py
# @Software: PyCharm

import json
import os
import random
import time
from multiprocessing import Process,Lock

def check():
    time.sleep(1)
    with open('ticket.txt','r',encoding='utf-8') as fp:
        dic = json.load(fp)
    print("%s 查看了剩余的票数 %s" %(os.getpid(),dic["count"]))


def buy():
    time.sleep(2)
    with open('ticket.txt','r',encoding='utf-8') as fp:
        dic = json.load(fp)

    if dic["count"] > 0:
        # 可以购买
        dic["count"] -= 1
        time.sleep(random.randint(1,3))
        with open('ticket.txt','w',encoding='utf-8') as fp:
            json.dump(dic,fp)
        print("%s 购买成功" %os.getpid())
    else:
        # 不能购买
        print("%s 购买失败" %os.getpid())

def task(mutex):
    check()

    # 给事件加锁，同一时间只有一个进程可以访问，加锁之后一定要释放
    mutex.acquire()
    buy()
    mutex.release()


if __name__ == "__main__":
    mutex = Lock() #互斥锁
    for i in range(10):
        p = Process(target=task,args={mutex,})
        p.start()

# join  会等待所有的子进程执行完毕 程序变成串行的
# mutex 互斥锁会将共享的数据操作，变成串行 虽然效率降低了，但是安全性和数据完整性提升



