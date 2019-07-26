#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/26 15:40
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : socket1.py
# @Software   : PyCharm
# @Description: 套接字 - 基于TCP协议创建时间服务器

from socket import *
from time import *


server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 6789))
server.listen()
print('服务器已经启动正在监听客户端连接...')
while True:
    client, addr = server.accept()
    print('客户端%s:%d连接成功.' % (addr[0], addr[1]))
    currtime = localtime(time())
    timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
    client.send(timestr.encode('utf-8'))
    client.close()
server.close()