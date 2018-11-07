import os, sys
import qtawesome as qta
from PySide2 import QtCore, QtWidgets, QtGui

class LeftItem(QtWidgets.QGroupBox):
    def mousePressEvent(self, event):
        if self.active:
            pass
        else:
            self.active=True
            self.item_icon.setStyleSheet("background-color:yellow; margin-top:0;")
            self.item_label.setStyleSheet("color:yellow; border-bottom-width:3px; border-bottom-style:solid; border-color:yellow;")
            self.item_count.setStyleSheet("color:yellow; border-bottom-width:3px; border-bottom-style:solid;")
            self.setStyleSheet("background-color:black; margin-top:0;")

    def enterEvent(self, event):
        if self.active:
            pass
        else:
            self.item_label.setStyleSheet("color:white; border-bottom-width:3px; border-bottom-style:solid;")
            self.item_count.setStyleSheet("color:white; border-bottom-width:3px; border-bottom-style:solid;")

    def leaveEvent(self, event):
        if self.active:
            pass
        else:
            pass
        self.item_icon.setStyleSheet("background-color:transparent;")
        self.item_label.setStyleSheet("color:gray; border-bottom-width:3px; border-bottom-style:solid;")
        self.item_count.setStyleSheet("background-color:transparent; color:gray; border-bottom-width:3px; border-bottom-style:solid; ")
        self.setStyleSheet("background-color:black; margin-top:0;")

    def build_layout(self):
        item_layout = QtWidgets.QHBoxLayout()
        item_layout.setSpacing(0)
        item_layout.setContentsMargins(0, 0, 0, 0)
        return item_layout

    def build_icon(self, icon_id, icon_name):
        pix = qta.icon(icon_name, color='gray', color_active='yellow')
        item_icon = QtWidgets.QLabel(pixmap=pix.pixmap(36, 36))
        return item_icon

    def build_label(self, item_id, item_text):
        label_font = QtGui.QFont("Century Schoolbook L", 12, QtGui.QFont.Bold)
        item_label = QtWidgets.QLabel(text=item_text, font=label_font)
        item_label.setFixedHeight(34)
        item_label.setStyleSheet("color:gray; border-bottom-width:3px; border-bottom-style:solid; ")
        return item_label

    def build_item_count(self, item_id):
        item_count = QtWidgets.QLabel()
        item_count.setFont(QtGui.QFont("Century Schoolbook L", 12, QtGui.QFont.Bold))
        item_count.setText(' 17 ')
        item_count.setStyleSheet("color:gray; border-bottom-width:3px; border-bottom-style:solid;")
        return item_count

    def __init__(self, item_data):
        QtWidgets.QGroupBox.__init__(self)
        self.active=False

        self.setStyleSheet("background-color:black; margin-top:0;")
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.setFixedHeight(36)

        item_layout = self.build_layout()

        self.item_icon = self.build_icon(icon_id = item_data['id'], icon_name = item_data['icon_name'])
        item_layout.addWidget(self.item_icon)

        self.item_label = self.build_label(item_data['id'], item_data['text'])
        item_layout.addWidget(self.item_label)

        self.item_count = self.build_item_count(item_data['id'])
        item_layout.addWidget(self.item_count)

        item_layout.setStretch(0, 1)
        item_layout.setStretch(1, 10)
        item_layout.setStretch(2, 1)

        self.setLayout(item_layout)
        self.setObjectName(item_data['id'])


class LeftPanel(QtWidgets.QVBoxLayout):
    def create_objects(self):
        text, ok = QtWidgets.QInputDialog.getText(self.widgee, 'Input Dialog', 'Enter your name:')

    def assign_signals(event):
        pass

    def set_lists(self):
        self.left_items_list = [
            {'id':'search_bar',  'icon_name':'mdi.magnify', 'text':' SEARCH',  'function':self.create_objects},
            {},
            {'id':'peak_item',   'icon_name':'mdi.server',  'text':' PEAKS',   'function':self.assign_signals},
            {'id':'bot_item',    'icon_name':'mdi.robot',   'text':' BOTS',    'function':self.create_objects},
            {'id':'command_item','icon_name':'mdi.console', 'text':' COMMANDS','function':self.create_objects},
            {'id':'event_item',  'icon_name':'mdi.calendar','text':' EVENTS',  'function':self.assign_signals},
            {},
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
