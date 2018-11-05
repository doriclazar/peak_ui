import os, sys
import qtawesome as qta
from PySide2 import QtCore, QtWidgets, QtGui

class ClickableLabel(QtWidgets.QLabel):
    def __init__(self, function):
        QtWidgets.QLabel.__init__(self)

        self.function = function
        self.setFont(QtGui.QFont("Century Schoolbook L", 18, QtGui.QFont.Bold))

    def mousePressEvent(self, event):
        self.function()

    # def enterEvent(self, event):
    #     self.setStyleSheet("background-color:orange; color:white;")

    # def leaveEvent(self, event):
    #     self.setStyleSheet("background-color:transparent; color:gray;")


class LeftItem(QtWidgets.QGroupBox):
    def enterEvent(self, event):
        self.item_icon.setStyleSheet("background-color:orange;")
        self.item_label.setStyleSheet("color:orange;")
        self.item_count.setStyleSheet("background-color:orange; color:gray;")
        self.setStyleSheet("background-color:white; margin-top:0;")
    def leaveEvent(self, event):
        self.item_icon.setStyleSheet("background-color:transparent;")
        self.item_label.setStyleSheet("color:gray;")
        self.item_count.setStyleSheet("background-color:transparent; color:gray;")
        self.setStyleSheet("background-color:black; margin-top:0;")


    def __init__(self, item_data):
        QtWidgets.QGroupBox.__init__(self)

        self.setStyleSheet("background-color:black; margin-top:0;")
        self.setFixedSize(270, 46)

        item_layout = QtWidgets.QHBoxLayout()
        item_layout.setSpacing(0)
        item_layout.setContentsMargins(0, 0, 0, 0)

        self.item_icon = ClickableLabel(item_data[3])
        fa5_icon = qta.icon(item_data[1], color='gray', color_active='orange')
        self.item_icon.setPixmap(fa5_icon.pixmap(46, 46))
        self.item_icon.setFixedSize(46, 46)
        item_layout.addWidget(self.item_icon)

        self.item_label = ClickableLabel(item_data[3])
        self.item_label.setText(item_data[2])
        self.item_label.setFixedSize(190, 32)
        self.item_label.setStyleSheet("color:gray;")
        item_layout.addWidget(self.item_label)

        self.item_count = ClickableLabel(item_data[3])
        self.item_count.setText('17')
        self.item_count.setStyleSheet("color:gray;")
        item_layout.addWidget(self.item_count)

        self.setObjectName(item_data[0])
        self.setLayout(item_layout)


class LeftPanel(QtWidgets.QVBoxLayout):
    def create_objects(self):
        text, ok = QtWidgets.QInputDialog.getText(self.widgee, 'Input Dialog', 'Enter your name:')

    def assign_signals(event):
        pass

    def set_lists(self):
        self.left_items_list = [
                ('search_bar',  'mdi.magnify',       ' SEARCH',   self.create_objects),
                (),
                ('peak_item',   'mdi.server',' PEAKS',    self.assign_signals),
                ('bot_item',    'mdi.robot',        ' BOTS',     self.create_objects),
                ('command_item','mdi.console',     ' COMMANDS', self.create_objects),
                ('event_item',  'mdi.calendar', ' EVENTS',    self.assign_signals),
                (),
                ]

    def __init__(self, parent):
        self.widgee = QtWidgets.QWidget()
        QtWidgets.QVBoxLayout.__init__(self)
        self.set_lists()
        self.setSpacing(0)
        self.setContentsMargins(0,0,0,0)
        self.setObjectName('left_panel')
        for item_data in self.left_items_list:
            if len(item_data) == 0:
                self.addSpacerItem(QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Expanding))
            else:
                self.addWidget(LeftItem(item_data))
        self.addSpacerItem(QtWidgets.QSpacerItem(0, 600, QtWidgets.QSizePolicy.Expanding))
        parent.addLayout(self)
