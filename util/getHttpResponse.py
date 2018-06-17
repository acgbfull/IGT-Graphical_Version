#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
getHttpResponse函数的功能:
    发送http请求然后获取response.
"""

import urllib.request
import urllib.parse
import zlib
import time
from config import config
import logging


def getHttpResponse(url, numRetries = 3):
    decodeMethod = 'utf-8'                                                        # response的解码方式
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0'       # header的构造，user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    request = urllib.request.Request(url, headers=headers)                      # request的构造
    # 获取response
    try:
        response = urllib.request.urlopen(request, timeout=config.timeout)

        # 检测response的内容是否字符流，否则转换为字符流
        respInfo = response.info()
        if (("Content-Encoding" in respInfo) and (respInfo['Content-Encoding'] == "gzip")):
            response = zlib.decompress(response.read(), 16 + zlib.MAX_WBITS)  # urllib.request.urlopen(request).read()return: 一个 bytes对象
        else:
            response = response.read()


        response = response.decode(decodeMethod)
        # print(response)
    except Exception as error:
        if numRetries > 0:
            if hasattr(error, 'code') and 400 <= error.code < 600:
                time.sleep(1)
                return getHttpResponse(url, numRetries - 1)                     # recursively retry 5xx HTTP errors
        else:
            logging.getLogger("real_time_info").info("getHttpResponse Error: {0}: {1}".format(Exception, error))
        response = ""
    return response
