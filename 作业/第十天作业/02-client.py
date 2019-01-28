#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-28 14:55
# @Author  : zhangjiang
# @Site    : 
# @File    : 02-client.py
# @Software: PyCharm

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 连接指定的ip和端口号
client.connect(('127.0.0.1',8080))


# 通信循环
while True:
    msg = input("请输入:>>>>").strip()
    if len(msg) == 0 : continue
    # 发送数据服务器端才会继续往下走
    client.send(bytes(msg,encoding='utf-8'))

    # 接收服务器端的数据
    data = client.recv(1024)
    print('来自服务器端的数据' , data)

# 关闭链接
client.close()


'''
客户端可以发送一个空的字节给服务端，但是服务端并没有处理
'''