#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/26 15:58
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : socket5.py
# @Software   : PyCharm
# @Description: 使用socketserver模块创建时间服务器


from socketserver import TCPServer, StreamRequestHandler
from time import *


class EchoRequestHandler(StreamRequestHandler):

    def handle(self):
        currtime = localtime(time())
        timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
        self.wfile.write(timestr.encode('utf-8'))

server = TCPServer(('localhost', 6789), EchoRequestHandler)
server.serve_forever()
