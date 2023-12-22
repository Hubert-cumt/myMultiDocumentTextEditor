from PyQt5 import QtCore

from MainWindows import MainWindow


# 本文件是布局相关的功能实现

def func_pile(window: MainWindow):
    window.layout_type = 2
    if len(window.mdiArea.subWindowList()) > 1:
        window.mdiArea.cascadeSubWindows()


def func_horizontal(window: MainWindow):
    window.layout_type = 1
    wid_list = window.mdiArea.subWindowList()
    size = len(wid_list)
    if size > 0:
        position = QtCore.QPoint(0, 0)
        for w in wid_list:
            rect = QtCore.QRect(0, 0, window.mdiArea.width() / size, window.mdiArea.height())
            w.setGeometry(rect)
            w.move(position)
            position.setX(position.x() + w.width())


def func_vertical(window: MainWindow):
    window.layout_type = 0
    wid_list = window.mdiArea.subWindowList()
    size = len(wid_list)
    if size > 0:
        position = QtCore.QPoint(0, 0)
        for w in wid_list:
            rect = QtCore.QRect(0, 0, window.mdiArea.width(), window.mdiArea.height() / size)
            w.setGeometry(rect)
            w.move(position)
            position.setY(position.y() + w.height())