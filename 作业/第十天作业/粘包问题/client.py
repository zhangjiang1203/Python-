#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-29 15:53
# @Author  : zhangjiang
# @Site    : 
# @File    : client.py
# @Software: PyCharm

import socket
import platform
import struct

system = platform.system()
print('操作系统',system)
print('系统',platform.uname())

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 连接指定的ip和端口号
client.connect(('127.0.0.1',8080))


# 通信循环
client.send(bytes("hello",encoding='utf-8'))
client.send(bytes("step",encoding='utf-8'))
client.send(bytes("world",encoding='utf-8'))


# 关闭链接
client.close()
'''
客户端可以发送一个空的字节给服务端，但是服务端并没有处理
'''