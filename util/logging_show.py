#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LoggingShow类的功能:
    创建并定义了一个logger实例, 调用这个logger实例输出的信息不仅仅会在控制台中显示, 还会写入程序的日志文件中.
"""

import os
import logging


class LoggingShow():
    def __init__(self, projectPath):
        self.log_path = projectPath +"\\log.txt"

        # 创建一个logger实例
        self.logger = logging.getLogger("real_time_info")
        self.logger.setLevel("DEBUG")
        # 创建一个handler,用于写入log文件
        self.fh = logging.FileHandler(self.log_path)
        self.fh.setLevel("DEBUG")
        # 再创建一个handler，用于把信息输出到控制台
        self.ch = logging.StreamHandler()
        self.ch.setLevel("DEBUG")

        # 为logger添加handler
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    def get_logger(self):
        return self.logger

    def close(self):
        self.get_logger().removeHandler(self.ch)
        self.get_logger().removeHandler(self.fh)
