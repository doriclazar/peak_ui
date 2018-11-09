import os, sys
import qtawesome as qta
from ui.extra_items.clickable_label import ClickableLabel
from PySide2 import QtCore, QtWidgets, QtGui

class RightItem(QtWidgets.QFrame):
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
        QtWidgets.QFrame.__init__(self)

        self.setStyleSheet("background-color:yellow; margin-top:0;")
        self.setFixedSize(120, 80)

        item_layout = self.build_layout()
        self.setLayout(item_layout)


class RightPanel(QtWidgets.QVBoxLayout):
    def create_navbar(self):
        pass
    def navigate(self):
        pass

    def build_navigation(self):
        nav_bar = QtWidgets.QFrame()
        nav_bar.setStyleSheet("background-color:yellow;")
        nav_bar.setFixedHeight(36)
        nav_layout = QtWidgets.QHBoxLayout()
        nav_layout.setContentsMargins(0, 0, 0, 0)

        move_frame = QtWidgets.QFrame()
        move_frame.setFixedHeight(36)
        move_frame.setStyleSheet('QFrame {border: 1px solid grey; border-radius: 4px; margin-top:0;}')
        move_layout = QtWidgets.QHBoxLayout()
        #move_layout.setSpacing(0)
        move_layout.setContentsMargins(0, 0, 0, 0)

        for move_item_data in self.move_label_list:
            if len(move_item_data) == 0:
                move_layout.addSpacerItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding))
            else:
                move_item = ClickableLabel(move_item_data)
                move_item.setStyleSheet('border:none;')
                move_layout.addWidget(move_item)


        move_frame.setLayout(move_layout)
        nav_layout.addWidget(move_frame)

        nav_layout.addSpacerItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding))


        search_frame = QtWidgets.QFrame()
        search_frame.setFixedHeight(36)
        search_frame.setStyleSheet('QFrame {border: 1px solid grey; border-radius: 4px;}')

        search_layout = QtWidgets.QHBoxLayout()
        search_layout.setSpacing(0)
        search_layout.setContentsMargins(0, 0, 0, 0)

        search_button = ClickableLabel(self.search_list[0])
        search_input = QtWidgets.QLineEdit()
        search_input.setStyleSheet('border:none;')

        go_button = ClickableLabel(self.search_list[2])


        #search_button.setStyleSheet('background-color:red;')
        #go_button.setStyleSheet('background-color:red;')
        
        search_layout.addWidget(search_button)
        search_layout.addWidget(search_input)
        search_layout.addWidget(go_button)

        search_layout.setStretch(0, 1)
        search_layout.setStretch(1, 20)
        search_layout.setStretch(2, 1) 

        search_frame.setLayout(search_layout)

        nav_layout.addWidget(search_frame)


        nav_layout.addSpacerItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding))



        stretches = [3, 1, 6, 9]
        for stretch_index in range(len(stretches)):
            nav_layout.setStretch(stretch_index, stretches[stretch_index])

        nav_bar.setLayout(nav_layout)
        return nav_bar


    def set_lists(self):
        self.search_list = [
            {'id':'filter_icon',    'icon':'mdi.filter',    'func':None},
            {'id':'search_input',   'icon':None,            'func':self.navigate},
            {'id':'search_icon',    'icon':'mdi.magnify',   'func':None},
            ]

        self.move_label_list = [
            {'id':'back_button',    'icon':'mdi.menu-left', 'func':self.navigate},
            {'id':'forward_button', 'icon':'mdi.menu-right','func':self.navigate},
            {'id':'reload_button',  'icon':'mdi.reload',    'func':self.navigate},
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

            page_group = QtWidgets.QFrame(page)

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
