from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog, QTextEdit, QMessageBox

from MainWindows import MainWindow
import TextEdit
import FuncLayout


# 本文件是文件操作相关功能的实现

def func_new(window: MainWindow):
    file = TextEdit.TextEdit()
    window.mdiArea.addSubWindow(file)
    file.show()
    if window.layout_type == 0:
        FuncLayout.func_vertical(window)
    elif window.layout_type == 1:
        FuncLayout.func_horizontal(window)
    elif window.layout_type == 2:
        FuncLayout.func_pile(window)


def func_open(window: MainWindow):
    filename, filetype = QFileDialog.getOpenFileName(window, "打开文件", "C:",
                                                     "Text files (*.txt);;HTML files (*html)")
    if filename:
        for w in window.mdiArea.subWindowList():
            file = w.widget()
            if file.filename == filename:
                window.mdiArea.setActiveSubWindow(w)
                print(file.filename, filename)
                break
        else:
            window.load_file(filename)
            if window.layout_type == 0:
                FuncLayout.func_vertical(window)
            elif window.layout_type == 1:
                FuncLayout.func_horizontal(window)
            elif window.layout_type == 2:
                FuncLayout.func_pile(window)


def load_file(window: MainWindow, filename):
    fiel = TextEdit.TextEdit(filename)
    fiel.load()
    window.mdiArea.addSubWindow(fiel)
    fiel.show()


def func_save(window: MainWindow):
    if window.empty():
        return
    file = window.mdiArea.activeSubWindow()
    file = file.widget()
    if file is None or not isinstance(file, QTextEdit):
        return True
    file.save()


def func_save_as(window: MainWindow):
    if window.empty():
        return
    file = window.mdiArea.activeSubWindow()
    file = file.widget()
    path, _ = QFileDialog.getSaveFileName(window, 'Save File', './', "Text files (*.txt);;HTML files (*.html)")
    if path == '':
        return
    with open(path, 'w') as file_path:
        if 'html' in file.filename:
            file_path.write(file.toHtml())
        if 'txt' in file.filename:
            print("toPlainText")
            file_path.write(file.toPlainText())


def func_close(window: MainWindow, event):
    num_unsaved = 0
    for w in window.mdiArea.subWindowList():
        file = w.widget()
        if file.isModified():
            num_unsaved += 1
    if num_unsaved != 0:
        dlg = QMessageBox.warning(window, "MDT Editor", "{0}个文档尚未保存，是否关闭？"
                                  .format(num_unsaved)
                                  , QMessageBox.Yes | QMessageBox.No)
        if dlg == QMessageBox.Yes:
            QtCore.QCoreApplication.quit()
        elif dlg == QMessageBox.No:
            event.ignore()
