# 基于PyQt5的QTextEdit 做出一些修改
from PyQt5.QtCore import QFile, QFileInfo, QIODevice, QTextStream, Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTextEdit


class TextEdit(QTextEdit):
    Id = 1

    def __init__(self, filename="", parent=None):
        super(TextEdit, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.filename = filename
        if self.filename == " ":
            self.filename = "Untitled-{0}".format(TextEdit.Id)
