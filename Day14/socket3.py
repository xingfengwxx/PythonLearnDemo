#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/26 15:50
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : socket3.py
# @Software   : PyCharm
# @Description: 套接字 - 基于UDP协议Echo服务器


from socket import *


server = socket(AF_INET, SOCK_DGRAM)
server.bind(('localhost', 6789))
while True:
    data, addr = server.recvfrom(1024)
    server.sendto(data, addr)
server.close()
