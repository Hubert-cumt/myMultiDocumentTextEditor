from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from MainWindows import MainWindow
import FuncSearch

class SearchBoxCreator:
    @staticmethod
    def search_box_init(window: MainWindow):
        # 用于search功能
        window.count = 0
        window.sw_work = False

        # 新建SearchBox控件
        window.SearchBox = QWidget()
        # 设置控件模态显示
        window.SearchBox.setWindowModality(Qt.ApplicationModal)
        # 搜索框UI
        window.SearchBox.setWindowTitle("搜索框")
        window.SearchBox.keyword_label = QLabel('关键字:', window)
        window.SearchBox.replace_label = QLabel('替换为:', window)
        window.SearchBox.keyword_line = QLineEdit(window)
        window.SearchBox.replace_line = QLineEdit(window)
        window.SearchBox.search_button = QPushButton('搜索', window)
        window.SearchBox.replace_button = QPushButton('替换', window)

        # 布局管理
        window.SearchBox.label_v_layout = QVBoxLayout()  # 1
        window.SearchBox.line_v_layout = QVBoxLayout()  # 2
        window.SearchBox.button_h_layout = QHBoxLayout()  # 3
        window.SearchBox.label_line_h_layout = QHBoxLayout()  # 4
        window.SearchBox.all_v_layout = QVBoxLayout()  # 5

        # 将关键字标签和替换标签添加到垂直布局1
        window.SearchBox.label_v_layout.addWidget(window.SearchBox.keyword_label)  # 6
        window.SearchBox.label_v_layout.addWidget(window.SearchBox.replace_label)
        # 将关键字输入框和替换输入框添加到垂直布局2
        window.SearchBox.line_v_layout.addWidget(window.SearchBox.keyword_line)
        window.SearchBox.line_v_layout.addWidget(window.SearchBox.replace_line)
        # 将搜索按钮和替换按钮添加到水平布局3
        window.SearchBox.button_h_layout.addWidget(window.SearchBox.search_button)
        window.SearchBox.button_h_layout.addWidget(window.SearchBox.replace_button)
        # 将垂直布局1和垂直布局2添加到水平布局4
        window.SearchBox.label_line_h_layout.addLayout(window.SearchBox.label_v_layout)  # 7
        window.SearchBox.label_line_h_layout.addLayout(window.SearchBox.line_v_layout)
        # 将水平布局4和水平布局3添加到垂直布局5
        window.SearchBox.all_v_layout.addLayout(window.SearchBox.label_line_h_layout)
        window.SearchBox.all_v_layout.addLayout(window.SearchBox.button_h_layout)
        # 设置SearchBox的布局
        window.SearchBox.setLayout(window.SearchBox.all_v_layout)

