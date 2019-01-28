#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-28 14:55
# @Author  : zhangjiang
# @Site    : 
# @File    : 01-server.py
# @Software: PyCharm


import socket
# socket的分类
'''
1.基于文件的套接字 AF_UNIX  底层文件系统来通信
2.基于网络的套接字 AF_INET
3.私网地址(保留地址) 10开头  172开头  192开头 
4.本地回环地址 '127.0.0.1'
'''
# 1.买手机,基于网络的套接字还有一个基于文件的套接字  TCP协议就是流式协议
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 通常每个套接字地址(协议/网络地址/端口)只允许使用一次 服务关闭了立即收回8080端口
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# 2.插卡 (绑定IP和端口)
phone.bind(('127.0.0.1',8080))

# 3.开机(等待)
phone.listen(5)

# 4.等待来自客户端的请求 (阻塞)，返回的是客户端的连接和客户端的地址
conn ,addr = phone.accept()
print("来自客户端的请求")
print(addr)


while True:
    try:
        # 5.收取客户端发送的数据，recv函数收的字节必须大于0字节，不接收0bytes
        data = conn.recv(1024)
        print('来自客户端发送的数据', data)
        # 6.给客户端发送数据
        conn.send(data.upper())
    except

# 7.关闭服务器
conn.close()
