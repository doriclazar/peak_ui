import qtawesome as qta
from PySide2 import QtCore, QtWidgets, QtGui

class ClickableLabel(QtWidgets.QLabel):
    def __init__(self, item_data):
        QtWidgets.QLabel.__init__(self)

        self.function = item_data['func']
        pix = qta.icon(item_data['icon'], color='gray', color_active='yellow')
        self.setPixmap(pix.pixmap(34, 34))
        self.setFont(QtGui.QFont("Century Schoolbook L", 18, QtGui.QFont.Bold))

    def mousePressEvent(self, event):
        self.function()


