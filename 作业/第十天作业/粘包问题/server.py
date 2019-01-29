#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-29 15:53
# @Author  : zhangjiang
# @Site    : 
# @File    : server.py
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
# phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# 2.插卡 (绑定IP和端口)
phone.bind(('127.0.0.1',8080))

# 3.开机(等待)
phone.listen(5)
# 获取上线信息
conn ,addr = phone.accept()
# 收取三次信息
data = conn.recv(5)
print('来自客户端发送的数据', data)

data = conn.recv(4)
print('来自客户端发送的数据', data)

data = conn.recv(5)
print('来自客户端发送的数据', data)
# 7.关闭服务器
conn.close()


'''
就是不知道一次性提取多少字节的数据造成的，这就是粘包问题
'''
