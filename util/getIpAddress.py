#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GetIpAddress类的功能:
    向http://ip.chinaz.com查询指定域名的IP地址, 把IP地址用正则表达式匹配出来, 最后写入数据库中.
"""

from util.getHttpResponse import getHttpResponse
import re
import logging


class GetIpAddress():
    def __init__(self, view, database, domain):
        self.view = view
        self.database = database
        self.domain = domain
        self.url = "http://ip.chinaz.com/{0}".format(domain)
        self.ip = ""

    def start(self):
        try:
            httpResponse = getHttpResponse(self.url)
            self.reDomainToIpInfo(httpResponse)
            logging.getLogger("real_time_info").info(u"成功获取域名的IP地址")
            self.view.showTextBrowser(u"成功获取域名的IP地址")
        except Exception as error:
            logging.getLogger("real_time_info").info(u"获取域名的IP地址失败, Error：{0}: {1}".format(Exception, error))
            self.view.showTextBrowser(u"获取域名的IP地址失败, Error：{0}: {1}".format(Exception, error))

    def reDomainToIpInfo(self, httpResponse):
        domainToIpInfoPattren = re.compile(r'<span class="Whwtdhalf w15-0">(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</span>')        # 匹配网址对应的ip地址的正则表达式

        domainToIpInfo = domainToIpInfoPattren.findall(httpResponse)
        # print(httpResponse)

        # 因为cdn的存在, 一个网址可能对应多个ip地址, 所以需要用for循环把它们都存进去
        if domainToIpInfo:
            for record in domainToIpInfo:
                self.ip = record
                self.database.addDomainToIpInfo(self.domain, self.ip)
