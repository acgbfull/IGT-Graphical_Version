#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CreateHtml类功能:
    从数据库中读取数据,
    数据放入构造好的含html代码的字符串中,
    最后把上述的连接好的字符串替换模板html文件的标记位.
"""
import os
import datetime


class CreateHtml():
    def __init__(self, database, project_path, ipList, domainList): #, view, database
        #self.view = view
        self.database = database
        self.project_path = project_path
        self.ipList = ipList
        self.domainList = domainList
        self.results_content = ""

    def start(self):
        template_html_path = u"{0}\\data\\{1}".format(os.path.abspath('.'), "template_html.html")
        with open(template_html_path, 'r') as f:                  # 打开html文件模板
            template_html = f.read()

        self.target_container()
        self.site_container()
        self.ip_container()
        created = datetime.datetime.now().strftime('%a, %b %d %Y %H:%M:%S')

        results_html = template_html % (self.results_content, created)

        results_html_path = u"{0}\\{1}".format(self.project_path, "results.html")
        with open(results_html_path, 'w', encoding='utf-8') as f:                  # 打开html文件模板
            f.write(results_html)

    def target_container(self):
        # custom summary results table
        table_content_all = ''

        table_show = u'<a id="show-{0}" href="javascript:showhide(\'{1}\');"><p>[+] {2}</p></a>'.format("target", "target", "target")
        table_hide = u'<a id="hide-{0}" href="javascript:showhide(\'{1}\');"><p>[-] {2}</p><hr></a>'.format("target", "target", "target")

        row_header = u'<tr><th>{0}</th><th>{1}</th><th>{2}</th></tr>'.format("name", "count", "target")
        row_content = ""
        row_content += u'<tr><td>{0}</td><td class="centered">{1}</td><td>{2}</td></tr>\n'.format("site", len(self.domainList), ' '.join(self.domainList))
        row_content += u'<tr><td>{0}</td><td class="centered">{1}</td><td>{2}</td></tr>\n'.format("ip", len(self.ipList), ' '.join(self.ipList))

        table_content_all += '<div class="container">\n{0}\n{1}\n<table id="target">\n{2}\n{3}</table>\n</div>\n'.format(table_show, table_hide, row_header, row_content)
        self.results_content += table_content_all

    def site_container(self):
        site_container_content = ""
        for site in self.domainList:
            site_container_content += self.site_table(site)
        site_container_all = ""
        site_container_show = u'<a id="show-{0}" href="javascript:showhide(\'{1}\');"><p>[+] {2}</p></a>'.format("site", "site", "site")
        site_container_hide = u'<a id="hide-{0}" href="javascript:showhide(\'{1}\');"><p>[-] {2}</p><hr></a>'.format("site", "site", "site")
        site_container_all += '<div class="container">\n{0}\n{1}\n<div id="{2}">{3}</div>\n</div>\n'.format(site_container_show, site_container_hide, "site", site_container_content)
        self.results_content += site_container_all

    def site_table(self, site):
        table_content_all = ''

        table_show = u'<a id="show-{0}" href="javascript:showhide(\'{1}\');"><p>[+] {2}</p></a>'.format(site, site, site)
        table_hide = u'<a id="hide-{0}" href="javascript:showhide(\'{1}\');"><p>[-] {2}</p><hr></a>'.format(site, site, site)

        row_header0 = u'<table name="table" id="{0}">\n<tr><th>{1}</th></tr>\n'.format(site, "IP Address")
        row_content0 = ""
        for record in self.database.queryDomainToIpInfo(site):
            row_content0 += u'<tr><td>{0}</td></tr>\n'.format(record.ip)

        domain = "{0}.{1}".format(site.split('.')[-2], site.split('.')[-1])
        row_header1 = \
            u'<table name="table-1" id="{0}">\n<tr><th>{1}</th><th>{2}</th><th>{3}</th><th>{4}</th><th>{5}</th><th>{6}</th><th>{7}</th><th>{8}</th><th>{9}</th></tr>\n'\
                .format(site+ "-1", u"注册者名称", u"邮箱", u"电话号码", u"所属国家", u"所属地区", u"所属城市", u"注册日期", u"到期日期", u"注册商")
        row_content1 = ""
        for record in self.database.queryWhois(domain):
            row_content1 += u'<tr><td>{0}</td><td>{1}</td><td>{2}</td><td class="centered">{3}</td><td class="centered">{4}</td><td class="centered">{5}</td><td>{6}</td><td>{7}</td><td>{8}</td></tr>\n'\
                .format(record.r_name, record.r_e_mail, record.r_phone, record.country, record.province, record.city, record.r_date, record.e_date, record.s_registrar)

        row_header2 = u'<table name="table-2" id="{0}">\n<tr><th>{1}</th><th>{2}</th><th>{3}</th></tr>\n'.format(site + "-2", u"子域名个数", u"子域名", u"标题")
        row_content2 = ""
        for record in self.database.querySubDomain(domain):
            row_content2 += u'<tr><td class="centered">{0}</td><td>{1}</td><td>{2}</td></tr>\n'.format(record.row, record.sub_domain, record.title)

        row_end = "</table>\n"
        table_content = row_header0 + row_content0 + row_end + row_header1 + row_content1 + row_end + row_header2 + row_content2 + row_end
        table_content_all += '<div>\n{0}\n{1}\n{2}</div>\n'.format(table_show, table_hide, table_content)
        return table_content_all

    def ip_container(self):
        ip_container_content = ""
        for ip in self.ipList:
            ip_container_content += self.ip_table(ip)
        ip_container_all = ""
        ip_container_show = u'<a id="show-{0}" href="javascript:showhide(\'{1}\');"><p>[+] {2}</p></a>'.format("ip", "ip", "ip", )
        ip_container_hide = u'<a id="hide-{0}" href="javascript:showhide(\'{1}\');"><p>[-] {2}</p><hr></a>'.format("ip", "ip", "ip", )
        ip_container_all += '<div class="container">\n{0}\n{1}\n<div id="{2}">{3}</div>\n</div>\n'.format(ip_container_show, ip_container_hide, "ip", ip_container_content)
        self.results_content += ip_container_all

    def ip_table(self, ip):
        table_content_all = ''

        table_show = u'<a id="show-{0}" href="javascript:showhide(\'{1}\');"><p>[+] {2}</p></a>'.format(ip, ip, ip)
        table_hide = u'<a id="hide-{0}" href="javascript:showhide(\'{1}\');"><p>[-] {2}</p><hr></a>'.format(ip, ip, ip)

        row_header0 = u'<table name="table" id="{0}">\n<tr><th>{1}</th><th>{2}</th><th>{3}</th><th>{4}</th></tr>\n'.format(ip, "country", "region", "city", "idc")
        row_content0 = ""
        for record in self.database.queryIpInfo(ip):
            row_content0 += u'<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td></tr>\n'.format(record.country, record.region, record.city, record.idc)

        row_header1 = u'<table name="table-1" id="{0}">\n<tr><th>{1}</th><th>{2}</th><th>{3}</th></tr>\n'.format(ip + "-1", u"同IP域名个数", u"同IP域名", u"最后一次解析日期")
        row_content1 = ""
        for record in self.database.queryReverseIpInfo(ip):
            row_content1 += u'<tr><td class="centered">{0}</td><td>{1}</td><td>{2}</td></tr>\n'.format(record.row, record.s_domain, record.date)

        row_header2 = u'<table name="table-2" id="{1}">\n<tr><th>{0}</th</tr>\n'.format("nmap扫描结果", ip + "-2")
        row_content2 = ""
        for record in self.database.queryNmapResult(ip):
            row_content2 += u'<tr><td><pre>\n{0}</pre></td></tr>\n'.format(record.result)

        row_end = "</table>\n"
        table_content = row_header0 + row_content0 + row_end + row_header1 + row_content1 + row_end + row_header2 + row_content2 + row_end
        table_content_all += '<div>\n{0}\n{1}\n{2}</div>\n'.format(table_show, table_hide, table_content)
        return table_content_all
