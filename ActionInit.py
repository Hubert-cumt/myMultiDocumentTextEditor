from PyQt5.QtGui import QIcon

from MainWindows import MainWindow


# 本文件主要是对对应的Action初始化 并且配上相应的图标

def action_init(window: MainWindow):
    # 新建文件 new
    window.action_new.setIcon(QIcon('icons/new.png'))
    window.action_new.setToolTip('新建文件')
    window.action_new.setStatusTip('新建文件')

    # 打开文件 open
    window.action_open.setIcon(QIcon('icons/open.png'))
    window.action_open.setToolTip('打开文件')
    window.action_open.setStatusTip('打开文件')

    # 保存文件 save
    window.action_save.setIcon(QIcon('icons/save.png'))
    window.action_save.setToolTip('保存文件')
    window.action_save.setStatusTip('保存文件')

    # 另存为 save as
    window.action_save_as.setIcon(QIcon('icons/save_as.png'))
    window.action_save_as.setToolTip('文件另存为')
    window.action_save_as.setStatusTip('文件另存为')

    # 剪切 cut
    window.action_cut.setIcon(QIcon('icons/cut.png'))
    window.action_cut.setToolTip('剪切')
    window.action_cut.setStatusTip('剪切')

    # 复制 copy
    window.action_copy.setIcon(QIcon('icons/copy.png'))
    window.action_copy.setToolTip('复制')
    window.action_copy.setStatusTip('复制')

    # 粘贴 paste
    window.action_paste.setIcon(QIcon('icons/paste.png'))
    window.action_paste.setToolTip('粘贴')
    window.action_paste.setStatusTip('粘贴')

    # 字符 font
    window.action_font.setIcon(QIcon('icons/font.png'))
    window.action_font.setToolTip('字符设置')
    window.action_font.setStatusTip('字符设置')

    # 颜色 color
    window.action_color.setIcon(QIcon('icons/color.png'))
    window.action_color.setToolTip('颜色设置')
    window.action_color.setStatusTip('颜色设置')

    # 关于 about
    window.action_about.setIcon(QIcon('icons/about.png'))
    window.action_about.setToolTip('关于')
    window.action_about.setStatusTip('关于')

    # 搜索 search
    window.action_search.setIcon(QIcon('icons/search.png'))
    window.action_search.setToolTip('搜索')
    window.action_search.setStatusTip('搜索')

    # 平铺 Pile
    window.action_pile.setIcon(QIcon('icons/pile.png'))
    window.action_pile.setToolTip('平铺布局')
    window.action_pile.setStatusTip('平铺布局')

    # 水平布局 horizontal
    window.action_horizontal.setIcon(QIcon('icons/horizontal.png'))
    window.action_horizontal.setToolTip('水平布局')
    window.action_horizontal.setStatusTip('水平布局')

    # 垂直布局 vertical
    window.action_vertical.setIcon(QIcon('icons/vertical.png'))
    window.action_vertical.setToolTip('垂直布局')
    window.action_vertical.setStatusTip('垂直布局')

    # 左对齐 left
    window.action_left.setIcon(QIcon('icons/left.png'))
    window.action_left.setToolTip('左对齐')
    window.action_left.setStatusTip('左对齐')

    # 右对齐 right
    window.action_right.setIcon(QIcon('icons/right.png'))
    window.action_right.setToolTip('右对齐')
    window.action_right.setStatusTip('右对齐')

    # 居中对齐 center
    window.action_center.setIcon(QIcon('icons/center.png'))
    window.action_center.setToolTip('居中对齐')
    window.action_center.setStatusTip('居中对齐')

    # 撤销 undo
    window.action_undo.setIcon(QIcon('icons/undo.png'))
    window.action_undo.setToolTip('撤销')
    window.action_undo.setStatusTip('撤销')

    # 重做 redo
    window.action_redo.setIcon(QIcon('icons/redo.png'))
    window.action_redo.setToolTip('重做')
    window.action_redo.setStatusTip('重做')
