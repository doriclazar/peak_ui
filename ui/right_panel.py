import os, sys
from PySide2 import QtCore, QtWidgets, QtGui
class RightItem(QtWidgets.QHBoxLayout):
    def __init__(self, item_data):
        QtWidgets.QHBoxLayout.__init__(self)

        item_icon = ClickableLabel(item_data[3])
        pixmap = QtGui.QPixmap(os.path.join('images', item_data[1]), width=32, height=32)
        item_icon.setPixmap(pixmap.scaled(32, 32))
        item_icon.setMinimumSize(32, 32)
        item_icon.setMaximumSize(32, 32)
        item_icon.setStyleSheet("background-color:yellow;")
        self.addWidget(item_icon)

        item_label = ClickableLabel(item_data[3])
        item_label.setText(item_data[2])
        item_label.setMinimumSize(100, 32)
        item_label.setMaximumSize(100, 32)
        self.addWidget(item_label)

        item_count = ClickableLabel(item_data[3])
        item_count.setText('0')
        self.addWidget(item_count)

        self.setObjectName(item_data[0])


class RightPanel(QtWidgets.QVBoxLayout):
    def create_navbar(self):
        pass
    def navigate(self, position):
        pass

    def set_lists(self):
        self.navigation_list = [
                ('back_button', 'chevron-left.svg', '', self.navigate),
                ('reload_button', 'sync-alt.svg', '', self.navigate),
                ('forward_button', 'chevron-rigth.svg', '', self.navigate),
                (),
                ]

        self.item_list = [
            ()
            ]
        
        self.right_items_list = [self.navbar, (), self.item_grid]

    def __init__(self, parent):
        QtWidgets.QVBoxLayout.__init__(self)

        self.navbar = QtWidgets.QHBoxLayout()
        self.item_grid = QtWidgets.QGridLayout()

        self.set_lists()
        self.setObjectName('right_panel')

        for navbar_data in self.navigation_list:
            if len(navbar_data) == 0:
                self.addSpacerItem(QtWidgets.QSpacerItem(30, 0, QtWidgets.QSizePolicy.Expanding))
            else:
                pass
                #self.addWidget(navbar_item)

        '''
        for item_data in self.right_items_list:
            if len(item_data) == 0:
                self.addSpacerItem(QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Expanding))
            else:
                self.addLayout(RightItem(item_data))
        '''
        self.addSpacerItem(QtWidgets.QSpacerItem(900, 0, QtWidgets.QSizePolicy.Expanding))
        parent.addLayout(self)
