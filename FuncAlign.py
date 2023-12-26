from PyQt5.QtCore import Qt

from MainWindows import MainWindow


# 本文件是布局相关函数的实现

def func_left(window: MainWindow):
    if window.empty():
        return
    window.mdiArea.activeSubWindow().widget().setAlignment(Qt.AlignLeft)


def func_right(window: MainWindow):
    if window.empty():
        return
    window.mdiArea.activeSubWindow().widget().setAlignment(Qt.AlignRight)


def func_center(window: MainWindow):
    if window.empty():
        return
    window.mdiArea.activeSubWindow().widget().setAlignment(Qt.AlignCenter)
