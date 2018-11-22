#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 11:43 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : 生成器.py
# @Software: PyCharm

'''
生成器:只要函数内部包含有yield关键字，那么函数名()得到的结果就是生成器，并且不会执行函数内部代码
'''

def func():
    print("====>first")
    yield 1
    print("====>second")
    yield 2
    print("====>third")
    yield 3
    print("====>end")

g = func()
print(g)
# g就是一个生成器，可直接调用__iter__()和__next__()
# 生成器就是迭代器

def my_range(start,stop,step):
    while start < stop:
        yield start
        start += step
#执行函数得到生成器，本质就是迭代器
obj = my_range(1,7,2)#next调用一次少一次，不能往回，只能往后取值
print(obj.__next__())

for i in obj:
    print(i)



import time
def tail(filepath):
    with open(filepath,'rb') as f:
        f.seek(0,2)
        while True:
            line = f.readline()
            if line:
                yield line
            else:
                time.sleep(0.2)

def grep(pattern,lines):
    for line in lines:
        line = line.decode('utf-8')
        if pattern in line:
            yield line

for line in grep("404",tail('access.log')):
    print(line,end="")

with open('access.log','a',encoding='utf-8') as f:
    f.write('出错了404\n')