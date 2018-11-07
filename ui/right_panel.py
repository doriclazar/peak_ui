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

    def build_item(self, icon_name):
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
            if len(nav_item_data) == 0:
                nav_layout.addSpacerItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding))
            else:
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
        self.search_list = [
            {'id':'search_icon',    'icon':'mdi.magnify', 'func':None, 'class':QtWidgets.QLabel,   'lst':[]},
                ]
        self.nav_label_list = [
            {'id':'back_button',    'icon':'mdi.menu-left', 'func':self.navigate, 'class':QtWidgets.QLabel,   'lst':[]},
            {'id':'forward_button', 'icon':'mdi.menu-right','func':self.navigate, 'class':QtWidgets.QLabel,   'lst':[]},
            {'id':'reload_button',  'icon':'mdi.reload',    'func':self.navigate, 'class':QtWidgets.QLabel,   'lst':[]},
            {},
            {'id':'search_bar',     'icon':'mdi.file',    'func':self.navigate, 'class':QtWidgets.QGroupBox,'lst':self.search_list},
            ]

        self.item_list = [
                {}
                ]

        self.pages_list = [
            {'id':'peaks_page',     'icon':'mdi.server',   'title':'Peaks'},
            {'id':'bots_page',      'icon':'mdi.robot',    'title':'Bots'},
            {'id':'commands_page',  'icon':'mdi.console',  'title':'Commands'},
            {'id':'events_page',    'icon':'mdi.calendar', 'title':'Events'},
            ]
        
        #self.right_items_list = [self.navbar, (), self.item_grid]

    def __init__(self, parent):
        QtWidgets.QVBoxLayout.__init__(self)

        self.setObjectName('right_panel')
        self.set_lists()

        self.navbar = self.build_navigation()
        self.addWidget(self.navbar)

        stacked_widget = QtWidgets.QStackedWidget(objectName="stacked_widget")
        for page_data in self.pages_list:
            page = QtWidgets.QWidget()

            page_group = QtWidgets.QGroupBox(page)
            page_group.setTitle(page_data['title'])

            page_layout = QtWidgets.QVBoxLayout()
            page_layout.setSpacing(0)
            page_layout.setContentsMargins(0, 0, 0, 0)
            page_layout.addWidget(page_group)

            page.setLayout(page_layout)
            stacked_widget.addWidget(page)


        for item_data in self.item_list:
            if len(item_data) == 0:
                self.addSpacerItem(QtWidgets.QSpacerItem(30, 0, QtWidgets.QSizePolicy.Expanding))
            else:
                right_item = RightItem(navbar_data)
                self.addWidget(right_item)

        self.addWidget(stacked_widget)
        parent.addLayout(self)
