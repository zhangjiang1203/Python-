#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-29 16:28
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
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# 2.插卡 (绑定IP和端口)
phone.bind(('127.0.0.1',8080))

# 3.开机(等待) 只支持5个客户端
phone.listen(5)

# 循环接收所有的客户端消息
while True:
    # 4.等待来自客户端的请求 (阻塞)，返回的是客户端的连接和客户端的地址
    conn ,addr = phone.accept()
    print(addr)
    # 通信循环
    while True:
        try:
            # 5.收取客户端发送的数据，recv函数收的字节必须大于0字节，不接收0bytes
            data = conn.recv(1024)
            print('来自客户端发送的数据', data)
            if len(data) == 0 : break

            # # 6.给客户端发送数据
            # conn.send(data.upper())

            # 服务端执行命令，执行的结果返回给客户端
            import subprocess
            import struct
            obj = subprocess.Popen(data.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            # 发送一个长度给客户端,怎么把包打成一个固定长度的字节,利用struct进行打包生成一个固定长度的包发送过去
            # 在客户端在进行解包操作
            total_size = struct.pack("i",len(stdout)+len(stderr))

            # 返回给客户端一个header字典
            header_dict = {}


            conn.send(total_size)
            conn.send(stdout+stderr)
        except ConnectionResetError:
            print('hahah')
            break

# 7.关闭服务器
conn.close()
