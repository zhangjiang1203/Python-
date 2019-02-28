#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-28 11:17
# @Author  : zhangjiang
# @Site    : 
# @File    : 9.进程池之apply.py
# @Software: PyCharm

import os
import time
from multiprocessing import Pool ,Process
from threading import current_thread

def task(i):
    i += 1
    print(i)


if __name__ == "__main__":
    p = Pool(7)
    for i in range(200):
        p.apply(task,args=(i,)) #apple在这里就是同步执行的
        res = p.apply_async(task,args=(i,)) #这就是异步执行的，每次返回一个结果
        res.get()
