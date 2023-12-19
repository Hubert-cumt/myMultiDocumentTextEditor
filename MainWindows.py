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

        # 状态栏
        self.status_bar = self.statusBar()

        # ***************动作初始化***************
        # 文件动作
        self.new_action = QAction('新建', self)
        self.open_action = QAction('打开', self)
        self.save_action = QAction('保存', self)
        self.save_as_action = QAction('另存为..', self)
        # 文本操作动作
        self.cut_action = QAction('剪切', self)
        self.copy_action = QAction('复制', self)
        self.paste_action = QAction('粘贴', self)
        # 字符设置动作
        self.font_action = QAction('字体', self)
        self.color_action = QAction('颜色', self)
        # 布局动作
        self.actionHorizontal = QAction('水平', self)
        self.actionVertical = QAction('垂直', self)
        self.actionPile = QAction('平铺', self)
        self.actionLeft = QAction('左对齐', self)
        self.actionRight = QAction('右对齐', self)
        self.actionCenter = QAction('居中', self)
        # 修改动作
        self.actionDelete = QAction('删除', self)
        self.actionRecover = QAction('撤销', self)
        # 特殊动作
        self.about_action = QAction('关于', self)
        self.search_action = QAction('搜索', self)

        # 剪贴板设置
        self.mime_data = QMimeData()
        self.clipBoard = QApplication.clipboard()

        # ***************控件初始化***************
        self.menu_init()

    def menu_init(self):
        # 文件动作绑定
        self.file_menu.addAction(self.new_action)
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.save_as_action)
        self.file_menu.addSeparator()

        # 编辑动作绑定
        self.edit_menu.addAction(self.cut_action)
        self.edit_menu.addAction(self.copy_action)
        self.edit_menu.addAction(self.paste_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.font_action)
        self.edit_menu.addAction(self.color_action)

        # 视图动作绑定
        self.view_menu.addAction(self.actionPile)
        self.view_menu.addAction(self.actionHorizontal)
        self.view_menu.addAction(self.actionVertical)

        # 搜索动作绑定
        self.search_menu.addAction(self.search_action)

        # 关于动作绑定
        self.about_menu.addAction(self.about_action)










if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    test = MainWindow()
    test.show()
    sys.exit(app.exec_())
