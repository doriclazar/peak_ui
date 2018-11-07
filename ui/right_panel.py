import os, sys
import qtawesome as qta
from ui.extra_items.clickable_label import ClickableLabel
from PySide2 import QtCore, QtWidgets, QtGui

class RightItem(QtWidgets.QGroupBox):
    def build_layout(self):
        item_layout = QtWidgets.QHBoxLayout()
        item_layout.setSpacing(0)
        item_layout.setContentsMargins(0, 0, 0, 0)
        return item_layout

    def build_item(self):
        #item_label = ClickableLabel(item_data[3])
        item_label = QtWidgets.QLabel()
        item_label.setText(item_data[2])
        item_label.setMinimumSize(34, 34)
        item_label.setMaximumSize(34, 34)
        pix = qta.icon(icon_name, color='gray', color_active='orange')
        item_label.setPixmap(QtGui.QPixmap(pix.pixmap(34, 34)))
        self.addWidget(item_label)

        self.setObjectName(item_data[0])

    def __init__(self, item_data):
        QtWidgets.QGroupBox.__init__(self)

        self.setStyleSheet("background-color:yellow; margin-top:0;")
        self.setFixedSize(120, 80)

        item_layout = self.build_layout()
        self.setLayout(item_layout)

class RightPanel(QtWidgets.QVBoxLayout):
    def create_navbar(self):
        pass
    def navigate(self, position):
        pass

    def build_navigation(self):
        navbar = QtWidgets.QGroupBox()
        navbar.setStyleSheet("background-color:yellow; margin-top:0;")
        navbar.setFixedHeight(36)
        nav_layout = QtWidgets.QHBoxLayout()
        nav_layout.setSpacing(0)
        nav_layout.setContentsMargins(0, 0, 0, 0)
        for nav_item_data in self.nav_label_list:
            nav_item = ClickableLabel(nav_item_data)
            nav_layout.addWidget(nav_item)
        nav_layout.addSpacerItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding))


        nav_layout.setStretch(0, 1)
        nav_layout.setStretch(1, 1)
        nav_layout.setStretch(2, 1)
        nav_layout.setStretch(3, 20)

        navbar.setLayout(nav_layout)
        return navbar

        navbar.setLayout(nav_layout)

    def set_lists(self):
        self.nav_label_list = [
                {'id':'back_button',    'icon_name':'mdi.menu-left', 'text':'', 'function':self.navigate},
                {'id':'reload_button',  'icon_name':'mdi.reload',    'text':'', 'function':self.navigate},
                {'id':'forward_button', 'icon_name':'mdi.menu-right','text':'', 'function':self.navigate},
                ]

        self.item_list = [
                {}
                ]
        
        #self.right_items_list = [self.navbar, (), self.item_grid]

    def __init__(self, parent):
        QtWidgets.QVBoxLayout.__init__(self)

        self.setObjectName('right_panel')
        self.set_lists()

        self.navbar = self.build_navigation()
        self.addWidget(self.navbar)

        for item_data in self.item_list:
            if len(item_data) == 0:
                self.addSpacerItem(QtWidgets.QSpacerItem(30, 0, QtWidgets.QSizePolicy.Expanding))
            else:
                right_item = RightItem(navbar_data)
                self.addWidget(right_item)

        self.addWidget(QtWidgets.QGraphicsView())
        parent.addLayout(self)
