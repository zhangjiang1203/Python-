#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/1 3:52 PM
# @Author  : zhangjiang
# @Site    : 
# @File    : 05-fileAction.py
# @Software: PyCharm
#
# import sys
#
# if len(sys.argv) != 3:
#     print("Usage:cp source_file target_file")
#     sys.exit()
#
# source_file,target_file=sys.argv[1] ,sys.argv[2]
# with open(source_file,'rb') as f_read,open(target_file,'wb') as f_write:
#     for line in f_read:
#         f_write.write(line)


#文件光标移动
'''
f.read(3) 文件打开方式为文本模式时 代表读取3个字符
          文件打开方式为文本模式时 代表读取三个字节
'''
import time
def timer(func):
    def customtime(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        stop_time = time.time()
        print("run time is %s" %(stop_time - start_time))
        return res

    return customtime

@timer
def hahah():
    print("jiiushi ni")

hahah()