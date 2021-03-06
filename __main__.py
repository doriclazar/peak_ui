#!/usr/bin/env python3
import os, sys
from PySide2 import QtCore, QtGui, QtWidgets
from ui.menu import MenuBar
from ui.left_panel import LeftPanel
from ui.right_panel import RightPanel
#from ui.right_panel import NavigationBar, DataPanel


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.resize(800, 600)
    menu_bar = MenuBar(main_window)
    central_widget = QtWidgets.QWidget(main_window)

    content = QtWidgets.QHBoxLayout(central_widget)
    left_panel = LeftPanel(content)
    rigth_panel = RightPanel(content)
    content.setStretch(0, 1)
    content.setStretch(1, 4)

    main_window.setCentralWidget(central_widget)
    main_window.show()
    sys.exit(app.exec_())
