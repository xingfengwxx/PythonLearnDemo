#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/26 15:46
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : socket2.py
# @Software   : PyCharm
# @Description: 套接字 - 基于TCP协议创建时间客户端


from socket import *


client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 6789))
while True:
    data = client.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))
client.close()
