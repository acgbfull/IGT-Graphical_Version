#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
主函数
"""

import sys
from ui.gui import Ui_MainWindow
from ui.view import View
from controller.controller import Controller
from PyQt5 import QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    view = View(ui, MainWindow)  # View prep (gui)
    controller = Controller(view)  # Controller prep (communication between model and view)
    view.startConnections(controller)

    MainWindow.show()
    sys.exit(app.exec_())