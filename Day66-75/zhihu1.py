#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/8/1 14:37
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : zhihu1.py
# @Software   : PyCharm
# @Description: 获取知乎发现上的问题链接
import re
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


def main():
    headers = {'user-agent': 'Baiduspider'}
    proxies = {
        'http': 'http://122.114.31.177:808'
    }
    base_url = 'https://www.zhihu.com/'
    seed_url = urljoin(base_url, 'explore')
    resp = requests.get(seed_url,
                        headers=headers,
                        proxies=proxies)
    soup = BeautifulSoup(resp.text, 'lxml')
    href_rgex = re.compile(r'^/question')
    link_set = set()
    for a_tag in soup.find_all('a', {'href': href_rgex}):
        if 'href' in a_tag.attrs:
            href = a_tag.attrs['href']
            full_url = urljoin(base_url, href)
            link_set.add(full_url)
    print('Total %d question pages found.' % len(link_set))


if __name__ == '__main__':
    main()