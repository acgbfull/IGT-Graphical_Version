#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GetIpDomainList类的功能:
    对用户输入的IP地址和网站进行格式检查, 是否为空或者非法格式, 通过检查后把IP地址和网站分开并用变量存储起来.
"""

import re
import logging


# get ip, domain input , and projectName
class GetIpDomainList():
    def __init__(self, view):
        self.view = view
        self.projectName = ""
        self.ipList = []
        self.domainList = []
        self.inputTextVerifyValue = False
        self.logger = logging.getLogger("real_time_info")

    # 该模块的主函数
    def start(self):
        # get ip, domain input , and projectName
        ipDomainInputText = self.getIpDomainList()
        self.splitIpDomain(ipDomainInputText)
        # 返回 输入是否合法且不为空的判断值、默认的项目名称（用于不输入项目存储路径时存储运行结果的目录名）、输入的IP列表、输入的域名列表
        return self.inputTextVerifyValue, self.projectName, self.ipList, self.domainList

    # 获取用户于ui中输入的ip和site，然后调用splitIpDomain()方法
    def getIpDomainList(self):
        return self.view.ui.ipDomainTextinput.text()

    def splitIpDomain(self, ipDomainInputText):
        # 将输入的ip和site分离开和存到属性中，并检查逐个检查输入的ip和domain是否合法，否，则弹窗警告.
        # 然后设置inputTextVerifyValue=False并且返回GetIpDomainList.start()，Controller.start()检测到inputTextVerifyValue=False后退出，返回到点击“开始”按钮前
        ipPattern = re.compile(r'^((\d|([1-9]\d)|(1\d\d)|(2[0-4]\d)|([1-2][0-5][0-5]))\.){3}(\d|([1-9]\d)|([1-2][0-5][0-5]))$')
        domainPattern = re.compile(r'^([a-zA-Z0-9][-a-zA-Z0-9]{0,62}\.)+([a-zA-Z]{1,62})$')
        ipDomain = list(filter(None, ipDomainInputText.split(' ')))                                     # 用户的输入可能有连续的空格, split()会获取到空字符串, 所以之后要用filter把空字符串去掉, 返回值非list, 用list()转换

        if ipDomain:
            self.projectName = ipDomain[0]                                                                  # 默认的项目名称(用于不输入项目存储路径时存储运行结果的目录名)
            for tmp in ipDomain:
                # 逐个检查输入的ip和domain是否合法，否，则弹窗警告; 是则作为list的元素存储到属性中, 到时直接返回list
                ip = ipPattern.search(tmp)
                domain = domainPattern.search(tmp)
                if (ip or domain):
                    if ip:
                        self.ipList.append(ip.group(0))
                    if domain:
                        self.domainList.append(domain.group(0))
                else:
                    self.inputTextVerifyValue = False
                    self.logger.info("-----------------------------------")
                    self.logger.info(u"存在输入的域名/IP不符合格式, 请重新输入")
                    self.view.showTextBrowser()
                    self.view.showTextBrowser(u"存在输入的域名/IP不符合格式, 请重新输入")
                    self.view.alertWindow(u"存在输入的域名/IP不符合格式, 请重新输入")
                    return False
        else:
            self.inputTextVerifyValue = False
            self.logger.info("-----------------------------------")
            self.logger.info(u"输入的域名/IP为空, 请重新输入")
            self.view.showTextBrowser()
            self.view.showTextBrowser(u"输入的域名/IP为空, 请重新输入")
            self.view.alertWindow(u"输入的域名/IP为空, 请重新输入")
            return False
        self.inputTextVerifyValue = True
        self.logger.info("-----------------------------------")
        self.logger.info("需查询的IP地址：\n    " + ' '.join(self.ipList))
        self.logger.info("需查询的域名：\n    " + ' '.join(self.domainList))
        self.view.showTextBrowser()
        self.view.showTextBrowser("需查询的IP地址：    " + ' '.join(self.ipList))
        self.view.showTextBrowser("需查询的域名：    " + ' '.join(self.domainList))


if __name__ == '__main__':
    string = r'192.168.0.1 444.123.147.123 www.baidu.com k21iedzxd.234asdv3as2.sadf.com 14.123.147.1 8.322.122.250 301.201.546.12 12.12.12 232sad.asdf3.org 232sad.asdf3.or1g 2-32sad.asdf3.org 2_32sad.asdf3.org'