#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-27 11:06
# @Author  : zhangjiang
# @Site    : 
# @File    : server.py
# @Software: PyCharm

import socket
import struct
import json
import subprocess
import os

class MyTCPServer:
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    max_packet_size = 8192
    coding = 'utf-8'
    request_queue_size = 5
    server_dir = "file_upload"

    def __init__(self,server_address,bind_and_activate=True):
        self.server_address = server_address
        self.socket = socket.socket(self.address_family,self.socket_type)

        if bind_and_activate:
            try:
                self.server_bind()
                self.server_activate()
            except:
                self.server_close()
                raise

    def server_bind(self):
        '''
        绑定服务
        :return:
        '''
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()

    def server_activate(self):
        '''
        开始监听
        :return:
        '''
        self.socket.listen(self.request_queue_size)

    def server_close(self):
        '''
        关闭服务
        :return:
        '''
        self.socket.close()


    def get_request(self):
        '''
        获取request和客户端的地址
        :return:
        '''
        return self.socket.accept()

    def close_request(self,request):
        '''
        开始清理request
        :param request:
        :return:
        '''
        request.close()

    def run(self):
        '''
        获取存储文件信息
        :return:
        '''
        while True:
            self.conn,self.client_address = self.get_request()
            print("\033[31m 客户端地址：%s\033[0m" %self.client_address)
            while True:
                try:
                    head_struct = self.conn.recv(4)
                    if not head_struct:break

                    head_len = struct.unpack("i",head_struct)[0]
                    head_json = self.conn.recv(head_len).decode(self.coding)
                    head_dic = json.loads(head_json)

                    print("\033[31m获取的数据 %s \033[0m" %head_dic)
                    cmd = head_dic["cmd"]
                    if hasattr(self,cmd):
                        func = getattr(self,cmd)
                        func(head_dic)
                except Exception:
                    break


    def put(self,args):
        '''
        存放数据
        :param args:
        :return:
        '''
        file_path = os.path.normpath(os.path.join(self.server_dir,args['filename']))
        file_size = args["filesize"]
        recv_size = 0
        print("\033[33m上传数据地址---> %s \033[0m" % file_path)
        with open(file_path,'wb') as f_w:
            while recv_size < file_size:
                recv_data = self.conn.recv(self.max_packet_size)
                f_w.write(recv_data)
                recv_size += len(recv_data)
                print("\033[33m 上传数据 %s  总文件大小：%s---> %s \033[0m" %(recv_size,file_size))


tcpserver = MyTCPServer(('127.0.0.1',8080))
tcpserver.run()



