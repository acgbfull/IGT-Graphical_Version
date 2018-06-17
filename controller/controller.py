#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Controller类控制整个软件运行流程.
"""

from db.database import Database
from util.logging_show import LoggingShow
from util.getIpDomainList import GetIpDomainList
from util.createFolderForResult import CreateFolderForResult
from util.getIpInfo import GetIpInfo
from util.getReverseIpInfo import GetReverseIpInfo
from util.getIpAddress import GetIpAddress
from util.getSubDomain import GetSubDomain
from util.whois import Whois
from util.nmapScan import nmapScan
from util.create_html import CreateHtml
import webbrowser
import sys


class Controller():
    """initialisations that will happen once - when the program is launched
    """
    def __init__(self, view):
        self.version = 'Information Gathering Tool 0.9 (BETA)'  # update this everytime you commit!
        self.view = view
        self.ipList = []
        self.domainList = []
        self.tempIpList = []
        self.tempDomainList = []
        self.projectPath = ""
        self.projectName = ""
        self.projectPathText = ""
        self.nmapParameter = ""
        self.checkBoxStatus = {}
        self.inputTextVerifyValue = None
        self.logging_show = None
        self.logger = None

    def start(self):
        self.initialisation()                                                            # initialisations Values
        # check input valid or not, not return before click actionRun button
        if self.inputTextVerifyValue is False:
            return True
        try:
            self.database = Database(self.projectPath)                                              # sqlite数据库的初始化, 之后直接调用Database类相应的方法即可
        except Exception as error:
            self.logger.debug("-----------------------------------")
            self.logger.debug("Database Error: {0}: {1}".format(Exception, error))
            self.view.showLog()
            self.view.showLog("Database Error: {0}: {1}".format(Exception, error))
        self.isSelect()
        #self.child_process()                                                                       # 根据用户选择的功能调用不同子模块进行查询相关信息

        return True

    # 初始化controller类中调用子模块(类/函数)所需要传递的变量
    # 创建存储运行结果的目录
    # 获取用户选择的功能
    def initialisation(self):
        self.view.clearTextBrowser()

        self.checkBoxStatus = {}
        self.inputTextVerifyValue, self.projectName, self.ipList, self.domainList = GetIpDomainList(self.view).start()   # 获取 输入是否合法且不为空的判断值、默认的项目名称（用于不输入项目存储路径时存储运行结果的目录名）、输入的IP列表、输入的域名列表
        if self.inputTextVerifyValue:
            self.nmapParameter = "{0}".format(self.view.ui.nmapParameterTextinput.text())           # 获取用户输入的nmap参数, 输入中不应该含有ip
            self.projectPathText = "{0}".format(self.view.ui.projectFullPathTextinput.text())           # 获取用户输入的项目存储路径
            self.projectPath = CreateFolderForResult(self.view, self.projectName, self.projectPathText).start()     # 创建存储结果数据的目录，并获取目录的路径
            self.getCheckBoxStatus()                                                                # 获取用户选择的功能
            self.logging_show = LoggingShow(self.projectPath)
            self.logger = self.logging_show.get_logger()

    # 获取ui上用户勾选的功能
    def getCheckBoxStatus(self):
        # 获取ip function area用户选择的功能
        self.checkBoxStatus['ipInfoQuery'] = self.view.ui.ipInfoQuery.isChecked()
        self.checkBoxStatus['sameIpDomainQuery'] = self.view.ui.sameIpDomainQuery.isChecked()
        self.checkBoxStatus['portScan'] = self.view.ui.portScan.isChecked()

        # 获取idomain function area用户选择的功能
        self.checkBoxStatus['ipAddressQuery'] = self.view.ui.ipAddressQuery.isChecked()
        self.checkBoxStatus['whois'] = self.view.ui.whois.isChecked()
        self.checkBoxStatus['subDomainQuery'] = self.view.ui.subdomainQuery.isChecked()
        self.checkBoxStatus['subdomainTitleGet'] = self.view.ui.subdomainTitleGet.isChecked()

    def isSelect(self):
        ipListLength = len(self.ipList)
        self.logger.info("-----------------------------------")
        self.logger.info(u"开始收集目标信息")
        self.view.showTextBrowser()
        self.view.showTextBrowser(u"开始收集目标信息")
        for i, ip in enumerate(self.ipList):
            self.logger.info("-----------------------------------")
            self.logger.info(u"{0}\n正在处理第{1}个IP, 共{2}个".format(ip, i+1, ipListLength))
            self.view.showTextBrowser()
            self.view.showTextBrowser(u"{0}\n正在处理第{1}个IP, 共{2}个".format(ip, i+1, ipListLength))

            if self.checkBoxStatus['ipInfoQuery']:
                GetIpInfo(self.view, self.database, ip).start()
            if self.checkBoxStatus['sameIpDomainQuery']:
                GetReverseIpInfo(self.view, self.database, ip).start()
            if self.checkBoxStatus['portScan']:
                nmapScan(self.view, self.database, ip, self.nmapParameter)

        domainListLength = len(self.domainList)
        for i, domain in enumerate(self.domainList):
            self.logger.info("-----------------------------------")
            self.logger.info(u"{0}\n正在处理第{1}个域名, 共{2}个".format(domain, i+1, domainListLength))
            self.view.showTextBrowser()
            self.view.showTextBrowser(u"{0}\n正在处理第{1}个域名, 共{2}个".format(domain, i+1, domainListLength))

            if self.checkBoxStatus['ipAddressQuery']:
                GetIpAddress(self.view, self.database, domain).start()
            if self.checkBoxStatus['whois']:
                Whois(self.view, self.database, domain).start()
            if self.checkBoxStatus['subDomainQuery']:
                GetSubDomain(self.view, self.database, self.checkBoxStatus['subdomainTitleGet'], domain).start()
        self.logger.info("-----------------------------------")
        self.logger.info(u"目标信息收集完毕")
        self.logger.info("-----------------------------------")
        self.view.showTextBrowser()
        self.view.showTextBrowser(u"目标信息收集完毕")
        self.view.showTextBrowser()

        self.logger.info(u"html文件生成中")
        self.view.showTextBrowser(u"html文件生成中")
        CreateHtml(self.database, self.projectPath, self.ipList, self.domainList).start()
        self.logger.info(u"html文件打开中")
        self.view.showTextBrowser(u"html文件打开中")
        webbrowser.open(u"{0}\\{1}".format(self.projectPath, "results.html"))
        self.logger.info("-----------------------------------")
        self.logger.info("执行完毕")
        self.view.showTextBrowser()
        self.view.showTextBrowser("执行完毕")
        self.logging_show.close()

    def kill_process(self):
        sys.exit("sorry, goodbye!")