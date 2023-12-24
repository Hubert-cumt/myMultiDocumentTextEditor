from MainWindows import MainWindow
import FuncLayout
import FuncFile
import FuncEdit


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
