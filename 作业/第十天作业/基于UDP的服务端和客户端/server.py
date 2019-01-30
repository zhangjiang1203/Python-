#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-30 13:35
# @Author  : zhangjiang
# @Site    : 
# @File    : server.py
# @Software: PyCharm


import socket

# 采用报文方式
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 绑定
server.bind(('127.0.0.1',8080))

# UDP不用监听，不用建立三次连接，返回的数据和绑定的地址
data,client_addr = server.recvfrom(1024)
print(data,client_addr)

# 回复消息
server.sendto(data.upper(),client_addr)

# 关闭服务
server.close()
