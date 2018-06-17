#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
View类为视图类, 对视图操作的方法都在此类.
"""

from PyQt5 import QtCore, QtWidgets


class View(QtCore.QObject):
    def __init__(self, ui, ui_mainwindow):
        QtCore.QObject.__init__(self)
        self.ui = ui
        self.ui_mainwindow = ui_mainwindow  # TODO: retrieve window dimensions/location from settings

        self.defaultCheckBoxStatus()
        #self.startOnce()
        #self.startConnections()

    def startConnections(self, controller):                                         # gui信号/槽关联
        self.controller = controller
        self.ui.actionRun.clicked.connect(self.controller.start)
        self.ui.actionPause.clicked.connect(self.controller.kill_process)
        self.ui.actionOpen.clicked.connect(self.openFile)

    def alertWindow(self, message = u"出现未知错误"):
        reply = QtWidgets.QMessageBox.information(self.ui.centralwidget, 'Warning', message, QtWidgets.QMessageBox.Yes)

    def showTextBrowser(self, message="-----------------------------------"):
        self.ui.logTextoutput.append(message)

    def clearTextBrowser(self):
        self.ui.logTextoutput.clear()

    def defaultCheckBoxStatus(self):
        self.ui.ipInfoQuery.setChecked(True)
        self.ui.sameIpDomainQuery.setChecked(True)
        self.ui.portScan.setChecked(True)

        self.ui.ipAddressQuery.setChecked(True)
        self.ui.whois.setChecked(True)
        self.ui.subdomainQuery.setChecked(True)
        self.ui.subdomainTitleGet.setChecked(True)

        self.ui.timeouotValue.setProperty("value", 5)

    def openFile(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(self.ui_mainwindow, "请选取含目标IP或网址的文本文件", "./project", "Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        if file_path[0]:
            with open(file_path[0], 'r') as f:
                if f:
                    file_content = f.read()
                    file_content = file_content.replace('\n', ' ')
                    self.ui.ipDomainTextinput.setText(file_content)
                else:
                    self.ui.ipDomainTextinput.setText(u"文件内容为空")
