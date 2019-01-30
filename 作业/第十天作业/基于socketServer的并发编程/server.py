#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-30 14:12
# @Author  : zhangjiang
# @Site    : 
# @File    : server.py
# @Software: PyCharm

import socketserver


class MyHandler(socketserver.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):
        '''
        处理所有的链接请求
        :return:
        '''
        while True:
            try:
                data = self.request.recv(1024)
                if len(data) == 0: break
                self.request.send(data.upper)
            except Exception as e:
                break

    def finish(self):
        pass

if __name__ == '__main__':
#     多开一个线程来服务客户端
      s = socketserver.ThreadingTCPServer(('127.0.0.1',8080),RequestHandlerClass=MyHandler,bind_and_activate=True)
      s.serve_forever()


