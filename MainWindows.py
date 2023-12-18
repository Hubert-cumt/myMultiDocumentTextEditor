import sys
import TextEdit
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPalette, QTextCursor, QTextDocument
from PyQt5.QtCore import Qt, QMimeData, QFile, QFileInfo
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox, \
    QFontDialog, QColorDialog, QVBoxLayout, QWidget, QFileDialog, QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout


class MainWindow(QMainWindow, QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # ***************主窗体设置***************
        self.setWindowTitle("MDT Editor by 16214911")
        self.setWindowIcon(QIcon('icons/edit.png'))


