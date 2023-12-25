from PyQt5.QtWidgets import QFontDialog, QColorDialog

from MainWindows import MainWindow


# 本文件是编辑相关功能实现

def func_cut(window: MainWindow):
    if window.empty():
        return
    window.mdiArea.activeSubWindow().widget().cut()


def func_copy(window: MainWindow):
    if window.empty():
        return
    window.mdiArea.activeSubWindow().widget().copy()


def func_paste(window: MainWindow):
    if window.empty():
        return
    window.mdiArea.activeSubWindow().widget().paste()


def func_font(window: MainWindow):
    if window.empty():
        return
    font, ok = QFontDialog.getFont()
    if ok:
        window.mdiArea.activeSubWindow().widget().setCurrentFont(font)


def func_color(window: MainWindow):
    if window.empty():
        return
    color = QColorDialog.getColor()
    if color.isValid():
        window.mdiArea.activeSubWindow().widget().setTextColor(color)


