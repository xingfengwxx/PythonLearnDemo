#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/26 15:53
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : socket4.py
# @Software   : PyCharm
# @Description: 套接字 - 基于UDP协议创建Echo客户端


from socket import *


client = socket(AF_INET, SOCK_DGRAM)
while True:
    data_str = input('请输入：')
    client.sendto(data_str.encode('utf-8'), ('localhost', 6789))
    data, addr = client.recvfrom(1024)
    data_str = data.decode('utf-8')
    print('服务器回应：', data_str)
    if data_str == 'bye':
        break
client.close()
