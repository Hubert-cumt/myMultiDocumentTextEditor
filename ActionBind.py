import FuncDo
from MainWindows import MainWindow
import FuncLayout
import FuncFile
import FuncEdit
import FuncAbout
import FuncSearch
import FuncAlign
import FuncDo


# 本文件将功能函数与按钮绑定起来

def action_bind(window: MainWindow):
    # *******************布局相关功能函数**************************
    # 平铺布局
    window.action_pile.triggered.connect(lambda: FuncLayout.func_pile(window))
    window.action_pile.setShortcut('Ctrl+0')

    # 水平布局
    window.action_horizontal.triggered.connect(lambda: FuncLayout.func_horizontal(window))
    window.action_horizontal.setShortcut('Ctrl+1')

    # 垂直布局
    window.action_vertical.triggered.connect(lambda: FuncLayout.func_vertical(window))
    window.action_vertical.setShortcut('Ctrl+2')

    # *******************文件相关功能函数**************************
    # 创建
    window.action_new.triggered.connect(lambda: FuncFile.func_new(window))
    window.action_new.setShortcut('Ctrl+N')

    # 打开
    window.action_open.triggered.connect(lambda: FuncFile.func_open(window))
    window.action_open.setShortcut('Ctrl+O')

    # 保存
    window.action_save.triggered.connect(lambda: FuncFile.func_save(window))
    window.action_save.setShortcut('Ctrl+S')

    # 另存为
    window.action_save_as.triggered.connect(lambda: FuncFile.func_save_as(window))
    window.action_save_as.setShortcut('Ctrl+A')

    # *******************编辑相关功能函数**************************
    # 剪切
    window.action_cut.triggered.connect(lambda: FuncEdit.func_cut(window))
    window.action_cut.setShortcut('Ctrl+X')

    # 复制
    window.action_copy.triggered.connect(lambda: FuncEdit.func_copy(window))
    window.action_copy.setShortcut('Ctrl+C')

    # 粘贴
    window.action_paste.triggered.connect(lambda: FuncEdit.func_paste(window))
    window.action_paste.setShortcut('Ctrl+V')

    # 字符设置
    window.action_font.triggered.connect(lambda: FuncEdit.func_font(window))
    window.action_font.setShortcut('Ctrl+T')

    # 颜色设置
    window.action_color.triggered.connect(lambda: FuncEdit.func_color(window))
    window.action_color.setShortcut('Ctrl+R')

    # *******************关于功能函数——跳到本项目的Github**************************
    # 关于 无快捷键
    window.action_about.triggered.connect(lambda: FuncAbout.func_about())

    # *******************搜索相关功能函数——debug 12/25**************************
    window.action_search.triggered.connect(lambda: FuncSearch.func_search(window))
    window.action_search.setShortcut('Ctrl+F')
    # search box内功能函数绑定
    window.SearchBox.search_button.clicked.connect(lambda: FuncSearch.search_word(window))
    window.SearchBox.replace_button.clicked.connect(lambda: FuncSearch.replace_word(window))

    # *******************文件相关功能函数**************************
    # 左对齐
    window.action_left.triggered.connect(lambda: FuncAlign.func_left(window))

    # 右对齐
    window.action_right.triggered.connect(lambda: FuncAlign.func_right(window))

    # 居中对齐
    window.action_center.triggered.connect(lambda: FuncAlign.func_center(window))

    # *******************撤销相关功能函数**************************
    # undo
    window.action_undo.triggered.connect(lambda: FuncDo.func_undo(window))
    # redo
    window.action_redo.triggered.connect(lambda: FuncDo.func_redo(window))
