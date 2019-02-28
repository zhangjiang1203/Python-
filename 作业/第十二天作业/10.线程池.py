#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-28 11:32
# @Author  : zhangjiang
# @Site    : 
# @File    : 10.线程池.py
# @Software: PyCharm

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

import time

def task(i):
    print(i)
    time.sleep(1)
    return '展示数据==%s' %i


if __name__ == "__main__":
    t = ThreadPoolExecutor(20) #池子里面放20个线程,每次执行20个

    t_l = []
    for i in range(100):

        res = t.submit(task,i) #submit就是做了线程中的一个start操作，submit执行完之后返回的就是task函数的返回值
        t_l.append(res)

    t.shutdown() #合并进程池中的close和join的工作，停止提交任务，并等待子线程执行完毕

    #获取函数的返回值
    for temp in t_l:
        print(temp.result()) #调用result函数展示函数返回值
