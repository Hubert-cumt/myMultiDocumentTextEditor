import sys
import TextEdit
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPalette, QTextCursor, QTextDocument, QKeySequence
from PyQt5.QtCore import Qt, QMimeData, QFile, QFileInfo
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox, \
    QFontDialog, QColorDialog, QVBoxLayout, QWidget, QFileDialog, QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout


class MainWindow(QMainWindow, QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # ***************多窗口控件***************
        self.mdiArea = QtWidgets.QMdiArea()
        self.layout_type = 0

        # ***************主窗体设置***************
        self.setWindowTitle("MDT Editor by 16214911")
        self.setWindowIcon(QIcon('icons/edit.png'))
        self.setCentralWidget(self.mdiArea)
        self.resize(1200, 800)

        # 主窗体菜单栏
        self.file_menu = self.menuBar().addMenu('文件(F)')
        self.edit_menu = self.menuBar().addMenu('编辑(E)')
        self.view_menu = self.menuBar().addMenu('视图(V)')
        self.search_menu = self.menuBar().addMenu('搜索(S)')
        self.about_menu = self.menuBar().addMenu('关于')

        # 工具栏
        self.file_toolbar = self.addToolBar('文件')
        self.edit_toolbar = self.addToolBar('编辑')
        self.del_toolbar = self.addToolBar('删除')
        self.view_toolbar = self.addToolBar('视图')
        self.search_toolbar = self.addToolBar('搜索')

        # 状态栏
        self.status_bar = self.statusBar()

        # ***************动作初始化***************
        # 文件动作
        self.action_new = QAction('新建', self)
        self.action_open = QAction('打开', self)
        self.action_save = QAction('保存', self)
        self.action_save_as = QAction('另存为..', self)
        # 文本操作动作
        self.action_cut = QAction('剪切', self)
        self.action_copy = QAction('复制', self)
        self.action_paste = QAction('粘贴', self)
        # 字符设置动作
        self.action_font = QAction('字体', self)
        self.action_color = QAction('颜色', self)
        # 布局动作
        self.action_horizontal = QAction('水平', self)
        self.action_vertical = QAction('垂直', self)
        self.action_pile = QAction('平铺', self)
        self.action_left = QAction('左对齐', self)
        self.action_right = QAction('右对齐', self)
        self.action_center = QAction('居中', self)
        # 修改动作
        self.action_delete = QAction('删除', self)
        self.action_recover = QAction('撤销', self)
        # 特殊动作
        self.action_about = QAction('关于', self)
        self.action_search = QAction('搜索', self)

        # 剪贴板设置
        self.mime_data = QMimeData()
        self.clipBoard = QApplication.clipboard()

        # ***************控件初始化***************
        self.menu_init()
        self.toolbar_init()

    def menu_init(self):
        # 文件动作绑定
        self.file_menu.addAction(self.action_new)
        self.file_menu.addAction(self.action_open)
        self.file_menu.addAction(self.action_save)
        self.file_menu.addAction(self.action_save_as)
        self.file_menu.addSeparator()

        # 编辑动作绑定
        self.edit_menu.addAction(self.action_cut)
        self.edit_menu.addAction(self.action_copy)
        self.edit_menu.addAction(self.action_paste)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.action_font)
        self.edit_menu.addAction(self.action_color)

        # 视图动作绑定
        self.view_menu.addAction(self.action_pile)
        self.view_menu.addAction(self.action_horizontal)
        self.view_menu.addAction(self.action_vertical)

        # 搜索动作绑定
        self.search_menu.addAction(self.action_search)

        # 关于动作绑定
        self.about_menu.addAction(self.action_about)

    def toolbar_init(self):
        # 文件工具栏动作绑定
        self.file_toolbar.addAction(self.action_new)
        self.file_toolbar.addAction(self.action_open)
        self.file_toolbar.addAction(self.action_save)
        self.file_toolbar.addAction(self.action_save_as)
        # 编辑工具栏动作绑定
        self.edit_toolbar.addAction(self.action_cut)
        self.edit_toolbar.addAction(self.action_copy)
        self.edit_toolbar.addAction(self.action_paste)
        self.edit_toolbar.addAction(self.action_font)
        self.edit_toolbar.addAction(self.action_color)
        # 视图工具栏动作绑定
        self.view_toolbar.addAction(self.action_left)
        self.view_toolbar.addAction(self.action_center)
        self.view_toolbar.addAction(self.action_right)
        # 删除 / 撤销 工具栏动作绑定
        self.del_toolbar.addAction(self.action_delete)
        self.del_toolbar.addAction(self.action_recover)
        # 搜索工具栏动作绑定
        self.search_toolbar.addAction(self.action_search)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    test = MainWindow()
    test.show()
    sys.exit(app.exec_())
