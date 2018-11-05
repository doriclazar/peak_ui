import qtawesome as qta
import os, sys
from PySide2 import QtCore, QtGui, QtWidgets

class MenuBar(object):
    def create_peak(self):
        pass
    def create_bot(self):
        pass
    def create_command(self):
        pass
    def create_event(self):
        pass
    def open_file(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self.parent, 'Open file',
                '/home/doriclazar/Downloads/','HTML files (*.html);;Text files (*.txt)')[0]
        if path:
            op_file = QtCore.QFile(path)
            if op_file.open(QtCore.QIODevice.ReadOnly):
                stream = QtCore.QTextStream(op_file)
                text = stream.readAll()
                info = QtCore.QFileInfo(path)
                if info.completeSuffix() == 'html':
                    #self.editor.setHtml(text)
                    pass
                else:
                    #self.editor.setPlainText(text)
                    pass
                op_file.close()

    def save_all(self):
        pass
    def import_from_pebo(self):
        pass
    def export_all(self):
        pass
    def export_bots(self):
        pass
    def export_commands(self):
        pass
    def export_events(self):
        pass
    def print_all(self):
        pass
    def appearance_settings(self):
        pass
    def auth_settings(self):
        pass
    def config_settings(self):
        pass


    def set_lists(self):
        self.new_list = [
                ('new_peak_action',    'mdi.server-plus',  'Peak',    '',         'f102', [], self.create_peak),
                ('new_bot_action',     'mdi.robot',     'Bot',     '',         'f102', [], self.create_bot),
                ('new_command_action', 'mdi.console-line',  'Command', '',         'f102', [], self.create_command),
                ('new_event_action',   'mdi.calendar-plus',  'Event',   '',         'f102', [], self.create_event),
                ]

        self.export_list = [
                ('export_all',        'mdi.export',  'Everything',    '',         'f102', [], self.export_all),
                (),
                ('export_bot',         'mdi.robot',  'Bots',    '',         'f102', [], self.export_bots),
                ('export_commands',    'mdi.console',  'Commands','',         'f102', [], self.export_commands),
                ('export_events',      'mdi.calendar-export',  'Events',  '',         'f102', [], self.export_events),
                ]

        self.file_list = [
                ('new_action',         'mdi.folder-plus',     'New',    'Ctrl+N',  'f102', self.new_list, None),
                ('open_action',        'mdi.folder-open','Open',   'Ctrl+O',  'f2d2', [],  self.open_file),
                (),
                ('save_action',        'mdi.content-save',      'Save',   'Ctrl+S',  'f2d2', [],  self.save_all),
                (),
                ('import_action',      'mdi.file-import','Import', 'Ctrl+I',  'f221', [], self.import_from_pebo),
                ('export_action',      'mdi.file-export','Export', 'Ctrl+E',  'f211', self.export_list, None),
                (),
                ('print_action',       'mdi.printer',    'Print',  'Ctrl+P',  'f2d2', [], self.print_all),
                (),
                ('quit_action',        'mdi.power',  'Quit',   'Ctrl+W',  'f311', [], self.parent.close),
                ]

        self.edit_list = [
                ('undo_action',        'mdi.undo',  'Undo',      'Ctrl+Z',   'f102', [], self.open_file),
                ('redo_action',        'mdi.redo',  'Redo',      'Ctrl+Y',   'f102', [], self.open_file),
                (),
                ('cut_action',         'mdi.content-cut',   'Cut',       'Ctrl+X',   'f102', [], self.open_file),
                ('copy_action',        'mdi.content-copy',  'Copy',      'Ctrl+C',   'f102', [], self.open_file),
                ('paste_action',       'mdi.content-paste', 'Paste',     'Ctrl+V',   'f102', [], self.open_file),
                ]

        self.view_list = []
        self.window_list = [] 
        self.settings_list = [
                ('appearance_action',   'mdi.brush',   'Appearance',     '',     'f005', [], self.appearance_settings()),
                ('auth_action',   'mdi.lock-open',   'Authentication',     '',     'f005', [], self.auth_settings()),
                ('config_action',   'mdi.wrench',   'General',     '',     'f005', [], self.config_settings()),
                ]

        self.help_list = [
                ('help_action',        'mdi.help',   'Help',     'F1',     'f005', [], self.open_file),
                ('about_action',       'mdi.information-variant',   'About',    'F8',     'f005', [], self.open_file) 
                ]

        self.menu_bar_list = [
                ('file_menu',    'File',    'Alt+F', 'f002', self.file_list), 
                ('edit_menu',    'Edit',    'Alt+E', 'f002', self.edit_list), 
                ('view_menu',    'View',    'Alt+V', 'f002', self.view_list), 
                ('window_menu',  'Window',  'Alt+W', 'f002', self.window_list), 
                ('settings_menu','Settings','Alt+S', 'f002', self.settings_list), 
                ('help_menu',    'Help',    'Alt+H', 'f002', self.help_list), 
                ]

    def create_menubar(self):
        self.menu_bar = self.parent.menuBar()
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 799, 19))
        self.menu_bar.setObjectName("menu_bar")

        for menu_data in self.menu_bar_list:
            menu_item = self.menu_bar.addMenu(menu_data[1])
            menu_item.setObjectName(menu_data[0])

            for action_data in menu_data[4]:
                if len(action_data) == 0:
                    menu_item.addSeparator()

                elif len(action_data[5]) > 0:
                    action_icon = qta.icon(action_data[1], color='black', color_active='orange')
                    action_item = menu_item.addMenu(QtGui.QIcon(action_icon), action_data[2])
                    for sub_action_data in action_data[5]:
                        if len(sub_action_data) == 0:
                            action_item.addSeparator()

                        else: 
                            sub_action_icon = qta.icon(sub_action_data[1], color='black', color_active='orange')
                            sub_action_item = action_item.addAction(QtGui.QIcon(sub_action_icon), sub_action_data[2])
                            sub_action_item.setObjectName(sub_action_data[0])
                            sub_action_item.setShortcut(sub_action_data[3])
                            sub_action_item.triggered.connect(sub_action_data[6])
                            action_item.setObjectName(action_data[0])

                else:
                    action_icon = qta.icon(action_data[1], color='black', color_active='orange')
                    action_item = menu_item.addAction(QtGui.QIcon(action_icon), action_data[2])
                    action_item.setObjectName(action_data[0])
                    action_item.setShortcut(action_data[3])
                    action_item.triggered.connect(action_data[6])


        self.parent.setMenuBar(self.menu_bar)

    def __init__(self, parent):
        self.parent = parent
        self.parent.setObjectName("main_window")
        self.parent.resize(799, 600)
        self.central_widget = QtWidgets.QWidget(parent)
        self.central_widget.setObjectName("central_widget")
        self.set_lists()
        self.create_menubar()
