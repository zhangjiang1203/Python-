#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-15 14:57
# @Author  : zhangjiang
# @Site    : 
# @File    : 06-队列.py
# @Software: PyCharm

from multiprocessing import Queue

q = Queue(3)

q.put("你好")
q.put("我就是我")
q.put("还有什么")


print(q.get(block=True,timeout=2))
print(q.get(block=True,timeout=2))
print(q.get(block=True,timeout=2))
# 队列中没有数据的时候不会继续等待展示，这个时候会直接报错
print(q.get(block=True,timeout=2))
