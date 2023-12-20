from MainWindows import MainWindow


# 本文件是主类的相关初始化逻辑
def menu_init(window: MainWindow):
    # 文件动作绑定
    window.file_menu.addAction(window.action_new)
    window.file_menu.addAction(window.action_open)
    window.file_menu.addAction(window.action_save)
    window.file_menu.addAction(window.action_save_as)
    window.file_menu.addSeparator()

    # 编辑动作绑定
    window.edit_menu.addAction(window.action_cut)
    window.edit_menu.addAction(window.action_copy)
    window.edit_menu.addAction(window.action_paste)
    window.edit_menu.addSeparator()
    window.edit_menu.addAction(window.action_font)
    window.edit_menu.addAction(window.action_color)

    # 视图动作绑定
    window.view_menu.addAction(window.action_pile)
    window.view_menu.addAction(window.action_horizontal)
    window.view_menu.addAction(window.action_vertical)

    # 搜索动作绑定
    window.search_menu.addAction(window.action_search)

    # 关于动作绑定
    window.about_menu.addAction(window.action_about)


def toolbar_init(window):
    # 文件工具栏动作绑定
    window.file_toolbar.addAction(window.action_new)
    window.file_toolbar.addAction(window.action_open)
    window.file_toolbar.addAction(window.action_save)
    window.file_toolbar.addAction(window.action_save_as)
    # 编辑工具栏动作绑定
    window.edit_toolbar.addAction(window.action_cut)
    window.edit_toolbar.addAction(window.action_copy)
    window.edit_toolbar.addAction(window.action_paste)
    window.edit_toolbar.addAction(window.action_font)
    window.edit_toolbar.addAction(window.action_color)
    # 视图工具栏动作绑定
    window.view_toolbar.addAction(window.action_left)
    window.view_toolbar.addAction(window.action_center)
    window.view_toolbar.addAction(window.action_right)
    # 删除 / 撤销 工具栏动作绑定
    window.del_toolbar.addAction(window.action_delete)
    window.del_toolbar.addAction(window.action_recover)
    # 搜索工具栏动作绑定
    window.search_toolbar.addAction(window.action_search)


def status_bar_init(window):
    window.status_bar.showMessage('准备开始')
