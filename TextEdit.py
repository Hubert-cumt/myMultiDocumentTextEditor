# 本文件是基于PyQt5的QTextEdit的一个TextEdit 做出一些修改
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
            TextEdit.Id += 1
        self.document().setModified(False)
        self.windowName = QFileInfo(self.filename).fileName()
        self.setWindowTitle(self.windowName)

    def close_event(self, event):
        if self.document().isModified():
            dlg = QMessageBox.question(self, "MDT Editor", "是否保存对'{0}'的修改?"
                                       .format(self.windowName)
                                       , QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if dlg == QMessageBox.Yes:
                self.save()
            elif dlg == QMessageBox.No:
                self.close()
            else:
                event.ignore()

    def judge_modified(self):
        return self.document().isModified()

    def save(self):
        if self.filename.startswith("Untitled") or self.filename == '':
            self.filename = QFileDialog.getSaveFileName(self, "保存文件"
                                                        , self.filename
                                                        , "Text files (*.txt);;HTML files (*.html)")[0]
        # 为空认为用户取消了保存
        if self.filename == '':
            return
        self.windowName = QFileInfo(self.filename).fileName()
        with open(self.filename, 'w') as file_path:
            if 'html' in self.windowName:
                file_path.write(self.toHtml())
            if 'txt' in self.windowName:
                file_path.write(self.toPlainText())
        self.setWindowTitle(QFileInfo(self.filename).fileName())
        self.document().setModified(False)

    def load(self):
        file = None
        try:
            file = QFile(self.filename)
            if not file.open(QIODevice.ReadOnly):
                raise IOError(str(file.errorString()))
            stream = QTextStream(file)

            if 'html' in self.filename:
                self.setText(stream.readAll())
            elif 'txt' in self.filename:
                print("setPlainText")
                self.setPlainText(stream.readAll())

            self.document().setModified(False)
        except EnvironmentError as e:
            QMessageBox.warning(self, "加载失败", "不能加载 {0}"
                                .format(self.filename))
        finally:
            if file is not None:
                file.close()
        self.setWindowTitle(QFileInfo(self.filename).fileName())
