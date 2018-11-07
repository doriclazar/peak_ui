import qtawesome as qta
from PySide2 import QtCore, QtWidgets, QtGui

class ClickableLabel(QtWidgets.QLabel):
    def __init__(self, item_data):
        QtWidgets.QLabel.__init__(self)

        self.function = item_data['function']
        pix = qta.icon(item_data['icon_name'], color='gray', color_active='orange')
        self.setPixmap(pix.pixmap(34, 34))
        self.setFont(QtGui.QFont("Century Schoolbook L", 18, QtGui.QFont.Bold))

    def mousePressEvent(self, event):
        pass
        self.function()


