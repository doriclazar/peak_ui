import os, sys
import qtawesome as qta
from PySide2 import QtCore, QtWidgets, QtGui

class ClickableLabel(QtWidgets.QLabel):
    def __init__(self, function):
        QtWidgets.QLabel.__init__(self)
        self.function = function
        self.setFont(QtGui.QFont("Helvetica", 14, QtGui.QFont.Bold))

    def mousePressEvent(self, event):
        self.function()


class LeftItem(QtWidgets.QHBoxLayout):
    def __init__(self, item_data):
        QtWidgets.QHBoxLayout.__init__(self)

        item_icon = ClickableLabel(item_data[3])
        fa5_icon = qta.icon(item_data[1], color='gray', color_active='orange')
        pixmap = fa5_icon.pixmap(32, 32)
        item_icon.setPixmap(pixmap.scaled(32, 32))
        item_icon.setMinimumSize(32, 32)
        item_icon.setMaximumSize(32, 32)
        item_icon.setStyleSheet("background-color:black;")
        self.addWidget(item_icon)

        item_label = ClickableLabel(item_data[3])
        item_label.setText(item_data[2])
        item_label.setFont(QtGui.QFont("Century Schoolbook L", 14, QtGui.QFont.Bold))
        item_label.setMinimumSize(130, 32)
        item_label.setMaximumSize(130, 32)
        item_label.setStyleSheet("background-color:black; color:gray;")

        self.addWidget(item_label)

        item_count = ClickableLabel(item_data[3])
        item_count.setText('17')
        self.setAlignment(QtCore.Qt.AlignCenter)
        item_count.setStyleSheet("background-color:black;color:gray;")
        self.addWidget(item_count)

        self.setObjectName(item_data[0])


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
        self.setObjectName('left_panel')
        for item_data in self.left_items_list:
            if len(item_data) == 0:
                self.addSpacerItem(QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Expanding))
            else:
                self.addLayout(LeftItem(item_data))
        self.addSpacerItem(QtWidgets.QSpacerItem(0, 600, QtWidgets.QSizePolicy.Expanding))
        parent.addLayout(self)
