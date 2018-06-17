#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GetReverseIpInfo类的功能:
    向http://viewdns.info/reverseip/查询指定ip的同ip域名, 把域名用正则表达式匹配出来, 最后写入数据库中.
"""

from util.getHttpResponse import getHttpResponse
import re
import logging


class GetReverseIpInfo():
    def __init__(self, view, database, ip):
        self.view = view
        self.database = database
        self.ip = ip
        self.url = "http://viewdns.info/reverseip/?host={0}&t=1".format(ip)
        self.row = ""
        self.s_domain = ""
        self.date = ""

    def start(self):
        try:
            httpResponse = getHttpResponse(self.url)
            self.reReverseIpInfo(httpResponse)
            logging.getLogger("real_time_info").info(u"成功获取同ip网站信息")
            self.view.showTextBrowser(u"成功获取同ip网站信息")
        except Exception as error:
            logging.getLogger("real_time_info").info(u"获取同ip网站信息失败, Error：{0}: {1}".format(Exception, error))
            self.view.showTextBrowser(u"获取同ip网站信息失败, Error：{0}: {1}".format(Exception, error))

    def reReverseIpInfo(self, httpResponse):
        # 匹配的数据：IP地址，条数
        reverseIpInfoPattern1 = re.compile(r'Reverse IP results for (.*?)<br>==============<br><br>There are (.*?) domains hosted on this server', re.S)

        # 匹配的数据：二级域名，日期
        reverseIpInfoPattern2 = re.compile(r' <td>(.*?)</td><td align="center">(.*?)</td></tr>', re.S)

        reverseIpInfo1 = reverseIpInfoPattern1.search(httpResponse)
        reverseIpInfo2 = reverseIpInfoPattern2.findall(httpResponse)
        # print(httpResponse)
        if reverseIpInfo1:
            self.ip = reverseIpInfo1.group(1)
            self.row = reverseIpInfo1.group(2)

        if reverseIpInfo2:
            for record in reverseIpInfo2:
                self.s_domain = record[0]
                self.date = record[1]
                self.database.addReverseIpInfo(self.ip, self.row, self.s_domain, self.date)