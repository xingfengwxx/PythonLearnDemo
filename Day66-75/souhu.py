#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/8/2 10:06
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : souhu.py
# @Software   : PyCharm
# @Description: 多线程爬取“手机搜狐网”所有页面

from enum import unique, Enum
from random import random
from threading import current_thread
from time import sleep
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


@unique
class SpiderStatus(Enum):
    IDLE = 0
    WORKING = 1


def decode_page(page_bytes, charsets=('utf-8',)):
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
    return page_html


class Retry(object):

    def __init__(self, *, retry_times=3,
                 wait_secs=5, errors=(Exception, )):
        self.retry_times = retry_times
        self.wait_secs = wait_secs
        self.errors = errors

    def __call__(self, fn):

        def wrapper(*args, **kwargs):
            for _ in range(self.retry_times):
                try:
                    return fn(*args, **kwargs)
                except self.errors as e:
                    print(e)
                    sleep((random() + 1) * self.wait_secs)
            return None
        return wrapper()


class Spider(object):

    def __init__(self):
        self.status = SpiderStatus.IDLE

    @Retry()
    def fetch(self, current_url, *, charsets=('utf-8', ),
              user_agent=None, proxies=None):
        thread_name = current_thread().name
        print(f'[{thread_name}]: {current_url}')
        headers = {'user-agent': user_agent} if user_agent else {}
        resp = requests.get(current_url,
                            headers=headers, proxies=proxies)
        return decode_page(resp.content, charsets) \
            if resp.status_code == 200 else None

    def parse(self, html_page, *, domain='m.sohu.com'):
        soup = BeautifulSoup(html_page, 'lxml')
        for a_tag in soup.body.select('a[href]'):
            parser = urlparse(a_tag.attrs['href'])
            scheme = parser.scheme or 'http'
