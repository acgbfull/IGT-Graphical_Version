#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Whois类的功能:
    向http://viewdns.info/whois/查询指定域名的whois信息, 把whois信息用正则表达式匹配出来, 最后写入数据库中.
"""

from util.getHttpResponse import getHttpResponse
import re
import logging

class Whois():
    def __init__(self, view, database, domain):
        self.view = view
        self.database = database
        self.domain = "{0}.{1}".format(domain.split('.')[-2], domain.split('.')[-1])
        self.url = "http://viewdns.info/whois/?domain={0}".format(domain)
        self.r_name = ""
        self.r_e_mail = ""
        self.r_phone = ""
        self.country = ""
        self.province = ""
        self.city = ""
        self.r_date = ""
        self.e_date = ""
        self.s_registrar = ""


    def start(self):
        try:
            httpResponse = getHttpResponse(self.url)
            self.reWhois(httpResponse)
            logging.getLogger("real_time_info").info("成功获取域名的whois信息")
            self.view.showTextBrowser("成功获取域名的whois信息")
        except Exception as error:
            logging.getLogger("real_time_info").info("获取域名的whois信息失败, Error：{0}: {1}".format(Exception, error))
            self.view.showTextBrowser("获取域名的whois信息失败, Error：{0}: {1}".format(Exception, error))

    def reWhois(self, httpResponse):
        # 域名的注册人的名字、地址、邮箱地址、电话号码、域名注册时间、过期时间的正则表达式
        rNamePattren = re.compile(r'Registrant Organization: (.*?)<br>Registrant Street:')
        rEMailPattren = re.compile(r'Registrant Email: (.*?)<br>Registry Admin ID:')
        rPhonePattren = re.compile(r'Registrant Phone: (.*?)<br>Registrant Phone Ext:')
        countryPattren = re.compile(r'Registrant Country: (.*?)<br>Registrant Phone:')
        provincePattren = re.compile(r'Registrant State/Province: (.*?)<br>Registrant Postal Code:')
        cityPattren = re.compile(r'Registrant City: (.*?)<br>Registrant State/Province:')
        rDatePattren = re.compile(r'Creation Date: (.*?)<br>')
        eDatePattren = re.compile(r'Registrar Registration Expiration Date: (.*?)<br>')
        sRegistrarPattren = re.compile(r'Registrar: (.*?)<br>Registrar IANA ID:')

        # 获取域名的注册人的名字、地址、邮箱地址、电话号码、域名注册时间、过期时间
        rName = rNamePattren.search(httpResponse)
        rEMail = rEMailPattren.search(httpResponse)
        rPhone = rPhonePattren.search(httpResponse)
        country = countryPattren.search(httpResponse)
        province = provincePattren.search(httpResponse)
        city = cityPattren.search(httpResponse)
        rDate = rDatePattren.search(httpResponse)
        eDate = eDatePattren.search(httpResponse)
        sRegistrar = sRegistrarPattren.search(httpResponse)

        # 把whois信息写入数据库
        if True:
            if rName:
                self.r_name = rName.group(1)
            if rEMail:
                self.r_e_mail = rEMail.group(1)
            if rPhone:
                self.r_phone = rPhone.group(1)
            if country:
                self.country = country.group(1)
            if province:
                self.province = province.group(1)
            if city:
                self.city = city.group(1)
            if rDate:
                self.r_date = rDate.group(1)
            if eDate:
                self.e_date = eDate.group(1)
            if sRegistrar:
                self.s_registrar = sRegistrar.group(1)
        self.database.addWhois(self.domain, self.r_name, self.r_e_mail, self.r_phone, self.country, self.province, self.city, self.r_date, self.e_date, self.s_registrar)
