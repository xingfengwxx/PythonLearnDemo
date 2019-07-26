#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/18 13:52
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : timeclient.py
# @Software   : PyCharm
# @Description: 获取时间客户端

from socket import socket


def main():
    # 1.创建套接字对象默认使用IPv4和TCP协议
    client = socket()
    # 2.连接到服务器(需要指定IP地址和端口)
    client.connect(('192.168.0.103', 6789))
    # 3.从服务器接收数据
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()
