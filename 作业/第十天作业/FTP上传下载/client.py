#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-27 11:06
# @Author  : zhangjiang
# @Site    : 
# @File    : client.py
# @Software: PyCharm

import socket
import struct
import json
import os


class MyTCPClient:
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    max_packet_size = 8192
    coding = 'utf-8'
    request_queue_size = 5

    def __init__(self,server_address,connect=True):
        self.server_address = server_address
        self.socket = socket.socket(self.address_family,self.socket_type)

        if connect:
            try:
                self.client_connect()
            except:
                self.client_close()
                raise


    def client_connect(self):
        self.socket.connect(self.server_address)


    def client_close(self):
        self.socket.close()

    def run(self):
        while True:
            inp = input('>>:').strip()
            if not inp :continue
            l = inp.split()
            cmd = l[0]
            if hasattr(self,cmd):
                func = getattr(self,cmd)
                func(l)

    def put(self,args):
        cmd = args[0]
        filename = args[1]
        if not os.path.isfile(filename):
            print("file:%s 不存在"  %filename)
            return
        else:
            filesize = os.path.getsize(filename)

        head_dic = {"cmd":cmd,"filename":os.path.basename(filename),"filesize":filesize}
        print(head_dic)
        head_json = json.dumps(head_dic)
        head_json_bytes = bytes(head_json,encoding=self.coding)

        head_struct = struct.pack('i',len(head_json_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)
        send_size = 0
        with open(filename,'rb') as f:
            for line in f:
                self.socket.send(line)
                send_size += len(line)
                print('上传数据大小==%s' %send_size)
            else:
                print('上传成功')


cliet = MyTCPClient(('127.0.0.1',8080))
cliet.run()