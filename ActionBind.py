from MainWindows import MainWindow
import FuncLayout


# 本文件将功能函数与按钮绑定起来

def action_bind(window: MainWindow):
    # 布局相关功能函数
    # 平铺布局
    window.action_pile.triggered.connect(lambda: FuncLayout.func_pile(window))
    window.action_new.setShortcut('Ctrl+0')

    # 水平布局
    window.action_pile.triggered.connect(lambda: FuncLayout.func_horizontal(window))
    window.action_new.setShortcut('Ctrl+1')

    # 垂直布局
    window.action_pile.triggered.connect(lambda: FuncLayout.func_vertical(window))
    window.action_new.setShortcut('Ctrl+2')

