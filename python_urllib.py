#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


from urllib.request import urlopen, build_opener, HTTPCookieProcessor, Request
import json, ssl
from http import cookiejar
"""
参考文档:
https://www.cnblogs.com/zhangxinqi/p/9170312.html#_label3
https://blog.csdn.net/Ren_ger/article/details/81510939
"""
from urllib.parse import urlparse, urlunsplit, urlsplit, urlencode, urljoin, parse_qs, parse_qsl, quote, unquote

# url = 'http://httpbin.org/post'
# data = {'user': 'linchqd', 'pass': '123456'}
hdr = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
# req = Request(url, headers=hdr)
# res = urlopen(req, data=urlencode(data).encode())
# a = res.read()
# print(json.loads(a))
# base_url = 'https://movie.douban.com/j/search_subjects'
# data = {
#     'type': 'movie',
#     'tag': '热门',
#     'page_limit': 50,
#     'page_start': 0
# }
# context = ssl._create_unverified_context()
# url = '{}?{}'.format(base_url, urlencode(data))
# req = Request(url, headers=hdr)
# res = urlopen(req, context=context)
#
# for items in json.loads(res.read())['subjects']:
#     for k, v in items.items():
#         print("{}: {}\n".format(k, v))
