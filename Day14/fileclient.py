#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/18 17:25
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : fileclient.py
# @Software   : PyCharm
# @Description: 保存图片的客户端
from base64 import b64decode
from json import loads
from socket import socket

HOST = '192.168.0.103'
PORT = 12330


def main():
    client = socket()
    client.connect((HOST, PORT))
    # 定义一个保存二进制数据的对象
    in_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接收1024字节
    data = client.recv(1024)
    while data:
        # 将收到的数据拼接起来
        in_data += data
        data = client.recv(1024)
    # 将收到的二进制数据解码成JSON字符串并转换成字典
    # loads函数的作用就是将JSON字符串转成字典对象
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('../download/' + filename, 'wb') as f:
        f.write(b64decode(filedata))
    print('图片已保存.')


if __name__ == '__main__':
    main()
