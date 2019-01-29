#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-29 13:49
# @Author  : zhangjiang
# @Site    : 
# @File    : processTest.py
# @Software: PyCharm

# import subprocess
# # 执行一段命令，并返回展示的数据
# obj = subprocess.Popen('ls',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#
# # 正确结果
# stdout = obj.stdout.read()
# # 错误结果
# stderr = obj.stderr.read()
#
# print(stdout.decode('utf-8')+stderr.decode('utf-8'))


# 打包专用参数
import struct
# 打包格式，后面添加的数据长度展示
'''
i 打包成固定的4个字节
l 打包成固定的8个字节
d 打包成固定的8个字节


'''
res = struct.pack('i',9235325)
print(res,len(res))

res = struct.unpack('i',res)
print(res,res[0])