# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ui.ico_rc
import ctypes

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(736, 523)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userUseArea = QtWidgets.QGroupBox(self.centralwidget)
        self.userUseArea.setGeometry(QtCore.QRect(10, 0, 721, 181))
        self.userUseArea.setTitle("")
        self.userUseArea.setObjectName("userUseArea")
        self.ipDomainList = QtWidgets.QLabel(self.userUseArea)
        self.ipDomainList.setGeometry(QtCore.QRect(30, 10, 51, 21))
        self.ipDomainList.setObjectName("ipDomainList")
        self.nmapParameters = QtWidgets.QLabel(self.userUseArea)
        self.nmapParameters.setGeometry(QtCore.QRect(30, 70, 51, 21))
        self.nmapParameters.setObjectName("nmapParameters")
        self.timeout = QtWidgets.QLabel(self.userUseArea)
        self.timeout.setGeometry(QtCore.QRect(480, 150, 31, 21))
        self.timeout.setObjectName("timeout")
        self.ipDomainTextinput = QtWidgets.QLineEdit(self.userUseArea)
        self.ipDomainTextinput.setGeometry(QtCore.QRect(90, 10, 311, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.ipDomainTextinput.setFont(font)
        self.ipDomainTextinput.setText("")
        self.ipDomainTextinput.setClearButtonEnabled(False)
        self.ipDomainTextinput.setObjectName("ipDomainTextinput")
        self.nmapParameterTextinput = QtWidgets.QLineEdit(self.userUseArea)
        self.nmapParameterTextinput.setGeometry(QtCore.QRect(90, 70, 311, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.nmapParameterTextinput.setFont(font)
        self.nmapParameterTextinput.setObjectName("nmapParameterTextinput")
        self.timeouotValue = QtWidgets.QSpinBox(self.userUseArea)
        self.timeouotValue.setGeometry(QtCore.QRect(520, 150, 42, 22))
        self.timeouotValue.setObjectName("timeouotValue")
        self.label_4 = QtWidgets.QLabel(self.userUseArea)
        self.label_4.setGeometry(QtCore.QRect(570, 150, 121, 21))
        self.label_4.setObjectName("label_4")
        self.actionOpen = QtWidgets.QToolButton(self.userUseArea)
        self.actionOpen.setGeometry(QtCore.QRect(410, 10, 41, 21))
        self.actionOpen.setObjectName("actionOpen")
        self.actionRun = QtWidgets.QPushButton(self.userUseArea)
        self.actionRun.setGeometry(QtCore.QRect(460, 10, 121, 23))
        self.actionRun.setObjectName("actionRun")
        self.actionPause = QtWidgets.QPushButton(self.userUseArea)
        self.actionPause.setGeometry(QtCore.QRect(590, 10, 121, 23))
        self.actionPause.setObjectName("actionPause")
        self.projectFullPath = QtWidgets.QLabel(self.userUseArea)
        self.projectFullPath.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.projectFullPath.setObjectName("projectFullPath")
        self.projectFullPathTextinput = QtWidgets.QLineEdit(self.userUseArea)
        self.projectFullPathTextinput.setGeometry(QtCore.QRect(90, 40, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(False)
        self.projectFullPathTextinput.setFont(font)
        self.projectFullPathTextinput.setObjectName("projectFullPathTextinput")
        self.groupBox = QtWidgets.QGroupBox(self.userUseArea)
        self.groupBox.setGeometry(QtCore.QRect(420, 40, 131, 101))
        self.groupBox.setObjectName("groupBox")
        self.ipInfoQuery = QtWidgets.QCheckBox(self.groupBox)
        self.ipInfoQuery.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.ipInfoQuery.setObjectName("ipInfoQuery")
        self.sameIpDomainQuery = QtWidgets.QCheckBox(self.groupBox)
        self.sameIpDomainQuery.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.sameIpDomainQuery.setObjectName("sameIpDomainQuery")
        self.portScan = QtWidgets.QCheckBox(self.groupBox)
        self.portScan.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.portScan.setObjectName("portScan")
        self.ipInfoQuery.raise_()
        self.sameIpDomainQuery.raise_()
        self.portScan.raise_()
        self.label_4.raise_()
        self.groupBox_2 = QtWidgets.QGroupBox(self.userUseArea)
        self.groupBox_2.setGeometry(QtCore.QRect(560, 40, 151, 100))
        self.groupBox_2.setObjectName("groupBox_2")
        self.ipAddressQuery = QtWidgets.QCheckBox(self.groupBox_2)
        self.ipAddressQuery.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.ipAddressQuery.setObjectName("ipAddressQuery")
        self.whois = QtWidgets.QCheckBox(self.groupBox_2)
        self.whois.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.whois.setObjectName("whois")
        self.subdomainQuery = QtWidgets.QCheckBox(self.groupBox_2)
        self.subdomainQuery.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.subdomainQuery.setObjectName("subdomainQuery")
        self.subdomainTitleGet = QtWidgets.QCheckBox(self.groupBox_2)
        self.subdomainTitleGet.setGeometry(QtCore.QRect(10, 80, 141, 20))
        self.subdomainTitleGet.setObjectName("subdomainTitleGet")
        self.spiderWebsiteStructure = QtWidgets.QCheckBox(self.groupBox_2)
        self.spiderWebsiteStructure.setGeometry(QtCore.QRect(10, 120, 121, 16))
        self.spiderWebsiteStructure.setObjectName("spiderWebsiteStructure")
        self.webComponentDiscern = QtWidgets.QCheckBox(self.groupBox_2)
        self.webComponentDiscern.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.webComponentDiscern.setObjectName("webComponentDiscern")
        self.logTextoutput = QtWidgets.QTextBrowser(self.centralwidget)
        self.logTextoutput.setGeometry(QtCore.QRect(10, 190, 721, 281))
        self.logTextoutput.setObjectName("logTextoutput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Information_Gathering_Tool"))
        MainWindow.setWindowIcon(QtGui.QIcon(':/images/g2.jpg'))
        #MainWindow.setWindowIcon(QtGui.QIcon(':/images/g.png'))
        # MainWindow.setWindowIcon(QtGui.QIcon(':/images/g.ico'))
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
        self.ipDomainList.setText(_translate("MainWindow", "域名/IP: "))
        self.nmapParameters.setText(_translate("MainWindow", "nmap参数:"))
        self.timeout.setText(_translate("MainWindow", "超时: "))
        self.ipDomainTextinput.setToolTip(_translate("MainWindow", "例：www.viewdns.info 120.24.248.50 csdn.net"))
        self.ipDomainTextinput.setPlaceholderText(_translate("MainWindow", "例：www.viewdns.info 120.24.248.50 csdn.net"))
        self.nmapParameterTextinput.setToolTip(_translate("MainWindow", "默认参数为：-sS -sV --top-ports 100"))
        self.nmapParameterTextinput.setPlaceholderText(_translate("MainWindow", "默认参数为：-sS -sV --top-ports 100"))
        self.label_4.setText(_translate("MainWindow", "(秒 超时的页面丢弃)"))
        self.actionOpen.setText(_translate("MainWindow", "..."))
        self.actionRun.setText(_translate("MainWindow", "开始"))
        self.actionPause.setText(_translate("MainWindow", "退出"))
        self.projectFullPath.setText(_translate("MainWindow", "项目存储路径:"))
        self.projectFullPathTextinput.setToolTip(_translate("MainWindow", "默认存储于本工具project目录。输入格式：C:WindowsHelptest.com"))
        self.projectFullPathTextinput.setPlaceholderText(_translate("MainWindow", "默认存储于本工具project目录。输入格式：C:\\Windows\\Help\\test.com"))
        self.groupBox.setTitle(_translate("MainWindow", "ip function"))
        self.ipInfoQuery.setText(_translate("MainWindow", "IP信息获取"))
        self.sameIpDomainQuery.setText(_translate("MainWindow", "同IP网站信息获取"))
        self.portScan.setText(_translate("MainWindow", "端口扫描"))
        self.groupBox_2.setTitle(_translate("MainWindow", "domain function"))
        self.ipAddressQuery.setText(_translate("MainWindow", "IP地址获取"))
        self.whois.setText(_translate("MainWindow", "whois"))
        self.subdomainQuery.setText(_translate("MainWindow", "子域名获取"))
        self.subdomainTitleGet.setText(_translate("MainWindow", "子域名网站title获取"))
        self.spiderWebsiteStructure.setText(_translate("MainWindow", "爬取网站目录结构"))
        self.webComponentDiscern.setText(_translate("MainWindow", "Web组件识别"))

