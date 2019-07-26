#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/18 16:51
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : fileserver.py
# @Software   : PyCharm
# @Description: 使用多线程技术处理多个用户请求的服务器，该服务器会向连接到服务器的客户端发送一张图片。

from base64 import b64encode
from json import dumps
from socket import socket
from threading import Thread

HOST = '192.168.0.103'
PORT = 12330


def main():

    # 自定义线程类
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclent = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'mm_copy.jpg'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = data
            # 通过dumps函数将字典处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送JSON字符串
            self.cclent.send(json_str.encode('utf-8'))
            self.cclent.close()

    # 1.创建套接字对象并指定使用哪种传输服务
    server = socket()
    # 2.绑定IP地址和端口(区分不同的服务)
    server.bind((HOST, PORT))
    server.listen(512)
    print('服务器启动开始监听...')
    with open('mm.jpg', 'rb') as f:
        # 将二进制数据处理成base64再解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器')
        # 启动一个线程来处理客户端的请求
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()