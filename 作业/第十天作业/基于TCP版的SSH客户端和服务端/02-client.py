#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-29 11:18
# @Author  : zhangjiang
# @Site    : 
# @File    : 02-client.py
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
while True:
    msg = input("请输入:>>>>").strip()
    if len(msg) == 0 : continue
    # 发送数据服务器端才会继续往下走
    client.send(bytes(msg,encoding='utf-8'))
    ''' 处理粘包问题 '''
    # 获取前四个固定的字节，获取要接收的字节长度
    total_size = client.recv(4)
    total_size = struct.unpack('i',total_size)[0]
    # 根据接收的字节个数 分次获取数据
    recv_data = b''
    recv_size = 0
    while recv_size < total_size:
        data = client.recv(1024)
        recv_data += data
        recv_size += len(data)

    # 接收服务器端的数据
    data = client.recv(1024)
    print('来自服务器端的数据' , data.decode('utf-8'))

# 关闭链接
client.close()


'''
客户端可以发送一个空的字节给服务端，但是服务端并没有处理
'''