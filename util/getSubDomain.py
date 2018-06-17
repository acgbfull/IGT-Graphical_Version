#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GetSubDomain类的功能:
    向http://searchdns.netcraft.com/查询指定域名的子域名, 把子域名用正则表达式匹配出来, 最后写入数据库中.
"""

from util.getHttpResponse import getHttpResponse
from util.getSiteTitle import getSiteTitle
import re
import logging


class GetSubDomain():
    def __init__(self, view, database, subdomainTitleGet, domain):
        self.view =view
        self.database = database
        self.domain = "{0}.{1}".format(domain.split('.')[-2], domain.split('.')[-1])
        self.url = r"http://searchdns.netcraft.com/?restriction=site+ends+with&host={0}&lookup=wait..&position=limited".format(self.domain)
        self.row = ""
        self.sub_domain = ""
        self.subdomainTitleGet = subdomainTitleGet
        self.title = ""
        self.logger = logging.getLogger("real_time_info")


    def start(self):
        try:
            httpResponse = getHttpResponse(self.url)
            self.reSubDomain(httpResponse)
            self.logger.info(u"成功获取子域名信息")
            self.view.showTextBrowser(u"成功获取子域名信息")
            if self.subdomainTitleGet:
                self.logger.info(u"成功获取子域名对应网站标题信息")
                self.view.showTextBrowser(u"成功获取子域名对应网站标题信息")
        except Exception as error:
            self.logger.info("获取子域名信息失败, Error：{0}: {1}".format(Exception, error))
            self.view.showTextBrowser("获取子域名信息失败, Error：{0}: {1}".format(Exception, error))

    def reSubDomain(self, httpResponse):
        subDomainRowPattren = re.compile(r'<p align="center"><em>Found (.*?) site.?</em></p>')
        subDomainPattren = re.compile(r'<a href="http://toolbar.netcraft.com/site_report\?url=http.?://(.*?)">')

        subDomainRow = subDomainRowPattren.search(httpResponse)
        subDomain = subDomainPattren.findall(httpResponse)

        # 判断是否存在子域名，不存在则输出xx无子域名条数
        if subDomainRow:
            self.row = subDomainRow.group(1)
        else:
            self.logger.info(u"{0}无子域名条数".format(self.domain))
            self.view.showTextBrowser(u"{0}无子域名条数".format(self.domain))

        # 判断是否存在子域名，存在则把相应信息写入数据库。是否获取子域名对应网站的title，则看获取子域名title功能是否被选择
        if subDomain:
            for record in subDomain:
                self.sub_domain = record
                # 判断获取子域名title功能是否被选择，是则获取子域名对应网站的title
                if self.subdomainTitleGet:
                    self.title = getSiteTitle("http://{0}".format(self.sub_domain))
                    try:
                        self.database.addSubDomain(self.domain, self.row, self.sub_domain, self.title)
                    except Exception as error:
                        self.logger.error('Database Error：', Exception, ":", error, '\n')
                        self.view.showTextBrowser("Database Error：{0}: {1}\n".format(Exception, error))
                else:
                    try:
                        self.database.addSubDomain(self.domain, self.row, self.sub_domain, "")
                    except Exception as error:
                        self.logger.error('Database Error：', Exception, ":", error, '\n')
                        self.view.showTextBrowser("Database Error：{0}: {1}\n".format(Exception, error))
        else:
            self.logger.info(u"{0}无子域名".format(self.domain))
            self.view.showTextBrowser(u"{0}无子域名".format(self.domain))
