#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/18 9:44
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : mmdownloader.py
# @Software   : PyCharm
# @Description: 使用requests网络请求，创建线程下载图片


from threading import Thread
import requests


class DownloadHandler(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('../download/' + filename, 'wb') as f:
            f.write(resp.content)
        print('download complete: url=%s' % self.url)


def main():
    # 通过requests模块的get函数获取网络资源
    resp = requests.get(
        'http://gank.io/api/data/%E7%A6%8F%E5%88%A9/10/1')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['results']:
        url = mm_dict['url']
        # 通过多线程的方式实现突破下载
        DownloadHandler(url).start()


if __name__ == '__main__':
    main()
