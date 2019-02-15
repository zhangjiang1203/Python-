#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-13 16:20
# @Author  : zhangjiang
# @Site    : 
# @File    : 01-开启进程.py
# @Software: PyCharm
import time
from multiprocessing import Process

def task(x):
    print("%s is running" % x)
    time.sleep(2)
    print("%s is done" % x)

if __name__ == "__main__":
    # target给进程绑定事件 task为自己定义的函数,args=为一个元组 kwargs定义为一个字典，添加传递的参数信息
    # kwargs={"x":"子进程"}
    p = Process(target=task,args=('子进程',))
    # 操作系统申请资源(内存空间大小，子进程的Pid号等)
    p.start()
    print("主进程开始")