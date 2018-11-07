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
            {'id':'new_peak_action',   'icon':'mdi.server-plus',  'txt':'Peak',     'shrt':'',     'lst':[], 'func':self.create_peak},
            {'id':'new_bot_action',    'icon':'mdi.robot',        'txt':'Bot',      'shrt':'',     'lst':[], 'func':self.create_bot},
            {'id':'new_command_action','icon':'mdi.console-line', 'txt':'Command',  'shrt':'',     'lst':[], 'func':self.create_command},
            {'id':'new_event_action',  'icon':'mdi.calendar-plus','txt':'Event',    'shrt':'',     'lst':[], 'func':self.create_event},
            ]

        self.export_list = [
            {'id':'export_all',        'icon':'mdi.export',        'txt':'All',     'shrt':'',     'lst':[], 'func':self.export_all},
            {},
            {'id':'export_bot',        'icon':'mdi.robot',         'txt':'Bots',    'shrt':'',     'lst':[], 'func':self.export_bots},
            {'id':'export_commands',   'icon':'mdi.console',       'txt':'Commands','shrt':'',     'lst':[], 'func':self.export_commands},
            {'id':'export_events',     'icon':'mdi.calendar-export','txt':'Events', 'shrt':'',     'lst':[], 'func':self.export_events},
            ]

        self.file_list = [
            {'id':'new_action',        'icon':'mdi.folder-plus',   'txt':'New',    'shrt':'Ctrl+N','lst':self.new_list, 'funt':None},
            {'id':'open_action',       'icon':'mdi.folder-open',   'txt':'Open',   'shrt':'Ctrl+O','lst':[],  'func':self.open_file},
            {},
            {'id':'save_action',       'icon':'mdi.content-save',  'txt':'Save',   'shrt':'Ctrl+S','lst':[],  'func':self.save_all},
            {},
            {'id':'import_action',     'icon':'mdi.file-import',   'txt':'Import', 'shrt':'Ctrl+I','lst':[], 'func':self.import_from_pebo},
            {'id':'export_action',     'icon':'mdi.file-export',   'txt':'Export', 'shrt':'Ctrl+E','lst':self.export_list,'func':None},
            {},
            {'id':'print_action',      'icon':'mdi.printer',       'txt':'Print',  'shrt':'Ctrl+P','lst':[], 'func':self.print_all},
            {},
            {'id':'quit_action',       'icon':'mdi.power',         'txt':'Quit',   'shrt':'Ctrl+W','lst':[], 'func':self.parent.close},
            ]

        self.edit_list = [
            {'id':'undo_action',       'icon':'mdi.undo',          'txt':'Undo',   'shrt':'Ctrl+Z','lst':[], 'func':self.open_file},
            {'id':'redo_action',       'icon':'mdi.redo',          'txt':'Redo',   'shrt':'Ctrl+Y','lst':[], 'func':self.open_file},
            {},
            {'id':'cut_action',        'icon':'mdi.content-cut',   'txt':'Cut',    'shrt':'Ctrl+X','lst':[], 'func':self.open_file},
            {'id':'copy_action',       'icon':'mdi.content-copy',  'txt':'Copy',   'shrt':'Ctrl+C','lst':[], 'func':self.open_file},
            {'id':'paste_action',      'icon':'mdi.content-paste', 'txt':'Paste',  'shrt':'Ctrl+V','lst':[], 'func':self.open_file},
            ]

        self.view_list = []
        self.window_list = [] 
        self.settings_list = [
            {'id':'appearance_action', 'icon':'mdi.brush',         'txt':'Appearance','shrt':'',   'lst':[], 'func':self.appearance_settings},
            {'id':'auth_action',       'icon':'mdi.lock-open',     'txt':'Authentication','shrt':'','lst':[],'func':self.auth_settings},
            {'id':'config_action',     'icon':'mdi.wrench',        'txt':'General','shrt':'',      'lst':[], 'func':self.config_settings},
            ]

        self.help_list = [
            {'id':'help_action',       'icon':'mdi.help',          'txt':'Help',   'shrt':'F1',    'lst':[], 'func':self.open_file},
            {'id':'about_action',      'icon':'mdi.information',   'txt':'About',  'shrt':'F8',    'lst':[], 'func':self.open_file} 
            ]

        self.menu_bar_list = [
            {'id':'file_menu',    'txt':'File',    'shrt':'Alt+F', 'lst':self.file_list},
            {'id':'edit_menu',    'txt':'Edit',    'shrt':'Alt+E', 'lst':self.edit_list},
            {'id':'view_menu',    'txt':'View',    'shrt':'Alt+V', 'lst':self.view_list},
            {'id':'window_menu',  'txt':'Window',  'shrt':'Alt+W', 'lst':self.window_list},
            {'id':'settings_menu','txt':'Settings','shrt':'Alt+S', 'lst':self.settings_list},
            {'id':'help_menu',    'txt':'Help',    'shrt':'Alt+H', 'lst':self.help_list},
            ]

    def create_menubar(self):
        self.menu_bar = self.parent.menuBar()
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 799, 19))
        self.menu_bar.setObjectName("menu_bar")
        self.menu_bar.setStyleSheet('QMenuBar::selected, QMenuBar::item:pressed { background-color:black; color:white; }')

        for menu_data in self.menu_bar_list:
            menu_item = self.menu_bar.addMenu(menu_data['txt'])
            menu_item.setObjectName(menu_data['id'])
            menu_item.setStyleSheet('QMenu::item::selected { background-color:black; color:white; }')

            for action_data in menu_data['lst']:
                if len(action_data) == 0:
                    menu_item.addSeparator()

                elif len(action_data['lst']) > 0:
                    action_icon = qta.icon(action_data['icon'], color='black', color_active='yellow')
                    action_item = menu_item.addMenu(QtGui.QIcon(action_icon), action_data['txt'])
                    for sub_action_data in action_data['lst']:
                        if len(sub_action_data) == 0:
                            action_item.addSeparator()

                        else: 
                            sub_action_icon = qta.icon(sub_action_data['icon'], color='black', color_active='yellow')
                            sub_action_item = action_item.addAction(QtGui.QIcon(sub_action_icon), sub_action_data['txt'])
                            sub_action_item.setObjectName(sub_action_data['id'])
                            sub_action_item.setShortcut(sub_action_data['shrt'])
                            sub_action_item.triggered.connect(sub_action_data['func'])
                            action_item.setObjectName(action_data['id'])

                else:
                    action_icon = qta.icon(action_data['icon'], color='black', color_active='yellow')
                    action_item = menu_item.addAction(QtGui.QIcon(action_icon), action_data['txt'])
                    action_item.setObjectName(action_data['id'])
                    action_item.setShortcut(action_data['shrt'])
                    action_item.triggered.connect(action_data['func'])


        self.parent.setMenuBar(self.menu_bar)

    def __init__(self, parent):
        self.parent = parent
        self.parent.setObjectName("main_window")
        self.parent.resize(799, 600)
        self.central_widget = QtWidgets.QWidget(parent)
        self.central_widget.setObjectName("central_widget")
        self.set_lists()
        self.create_menubar()
