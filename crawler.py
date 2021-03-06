#!/usr/bin/env python
# coding=utf8

# version:1.0
# kali linux python 3.6
# author:TClion
# create:2018-12-31

import re
import argparse
import requests


parser = argparse.ArgumentParser()
parser.add_argument('-u')   # 指定爬虫开始地址
parser.add_argument('-d')   # 指定爬虫深度
parser.add_argument('--thread')     # 指定线程池大小，多线程爬取页面，可选参数，默认10
parser.add_argument('--dbfile')     # 存放结果数据到指定的数据库（sqlite）文件中
parser.add_argument('--key')    # 页面内的关键词，获取满足该关键词的网页，可选参数，默认为所有页面
parser.add_argument('-l')   # 日志记录文件记录详细程度，数字越大记录越详细，可选参数，默认spider.log
parser.add_argument('-testself')    # 程序自测，可选参数


def get_html(url):
    try:
        res = requests.get(url)
        text = res.text
    except:
        print('get page error')


if __name__ == '__main__':
    url = "http://www.baidu.com"
    get_html(url)