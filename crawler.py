#!/usr/bin/env python
# coding=utf8

# version:1.0
# kali linux python 3.6
# author:TClion
# create:2018-12-31

import requests


def get_html(url):
    try:
        res = requests.get(url)
        text = res.text
    except:
        print('get page error')


if __name__ == '__main__':
    url = "http://www.baidu.com"
    get_html(url)