#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
nmapScan函数的功能:
    调用nmap对指定ip进行扫描.
"""

import os
from config import config
import logging

def nmapScan(view, database, ip, nmapParameter):
    # 用户有输入nmap参数，则使用用户的输入；否则将读取config.py里的设置作为默认参数
    try:
        if nmapParameter:
            cmd = "{0} {1} {2}".format("nmap.exe", nmapParameter, ip)
        else:
            cmd = "{0} {1}".format(config.nmap_cmd_line, ip)
        logging.getLogger("real_time_info").info("{0}".format(cmd))
        view.showTextBrowser("{0}".format(cmd))
        result = os.popen(cmd).read()
        #print(ip, cmd, result)
        database.addNmapResult(ip, cmd, result)
        logging.getLogger("real_time_info").info("成功获取端口信息")
        view.showTextBrowser("成功获取端口信息")
    except Exception as error:
        logging.getLogger("real_time_info").info("获取端口信息失败, Error：{0}: {1}".format(Exception, error))
        view.showTextBrowser("获取端口信息失败, Error：{0}: {1}".format(Exception, error))
