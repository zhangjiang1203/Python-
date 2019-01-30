#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-30 13:35
# @Author  : zhangjiang
# @Site    : 
# @File    : client.py
# @Software: PyCharm

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 只需要知道服务端的ip和地址就可以实现通信
client.sendto("hello world".encode('utf-8'),('127.0.0.1',8080))

data = client.recvfrom(1024)
# 接收到的数据
print(data)

client.close()