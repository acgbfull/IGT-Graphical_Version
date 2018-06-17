#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GetIpInfo类的功能:
    通过http://freeapi.ipip.net/这个接口, 查询指定ip的地理位置等信息.
"""

from util.getHttpResponse import getHttpResponse
import re
import logging


class GetIpInfo():
    def __init__(self, view, database, ip):
        self.view = view
        self.database = database
        self.ip = ip
        self.url = "http://freeapi.ipip.net/{0}".format(ip)
        self.country = ""
        self.region = ""
        self.city = ""
        self.idc = ""

    def start(self):
        try:
            httpResponse = getHttpResponse(url=self.url, numRetries=6)
            self.reIpInfo(httpResponse)
            self.database.addIpInfo(self.ip, self.country, self.region, self.city, self.idc)
            logging.getLogger("real_time_info").info(u"成功获取ip信息")
            self.view.showTextBrowser(u"成功获取ip信息")
        except Exception as error:
            logging.getLogger("real_time_info").info(u"ip信息获取失败, Error: {0}: {1}".format(Exception, error))
            self.view.showTextBrowser(u"ip信息获取失败, Error: {0}: {1}".format(Exception, error))

    def reIpInfo(self, httpResponse):
        ipInfoPattern = re.compile(r'\["(.*?)","(.*?)","(.*?)","(.*?)","(.*?)"\]')      # 匹配ip对应的物理地址和idc的正则表达式

        ipInfo = ipInfoPattern.search(httpResponse)
        if ipInfo:
            self.country = ipInfo.group(1)
            self.region = ipInfo.group(2)
            self.city = ipInfo.group(3)
            self.idc = ipInfo.group(5)
