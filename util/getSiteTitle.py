#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
getSiteTitle函数的功能:
    对指定子域名发送http请求, 把response的<title></title>中的内容用正则表达式匹配出来, 最后写入数据库中.
"""

from util.getHttpResponse import getHttpResponse
import re


def getSiteTitle(site):
    httpResponse = getHttpResponse(site)
    titlePattren = re.compile(r'<title>(.*?)</title>')
    title = titlePattren.search(httpResponse)
    if title:
        return title.group(1)