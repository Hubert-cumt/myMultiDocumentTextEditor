import sys
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
        self.setWindowIcon(QIcon('icons/main.png'))
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
        self.action_undo = QAction('撤销', self)
        self.action_redo = QAction('重做', self)
        # 特殊动作
        self.action_about = QAction('关于', self)
        self.action_search = QAction('搜索', self)

        # 剪贴板设置
        self.mime_data = QMimeData()
        self.clipBoard = QApplication.clipboard()

        # ***************初始化***************
        import Init
        import SearchUI
        import ActionInit
        import ActionBind

        # 控件初始化
        Init.menu_init(self)
        Init.toolbar_init(self)
        Init.status_bar_init(self)
        SearchUI.SearchBoxCreator.search_box_init(self)

        # 动作初始化与连接
        ActionInit.action_init(self)
        ActionBind.action_bind(self)

    def empty(self):
        wid_list = self.mdiArea.subWindowList()
        if len(wid_list) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    test = MainWindow()
    test.show()
    sys.exit(app.exec_())
