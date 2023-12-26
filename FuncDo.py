from MainWindows import MainWindow


# 本文件是撤销和重做功能的具体实现

def func_redo(window: MainWindow):
    window.mdiArea.activeSubWindow().widget().redo()


def func_undo(window: MainWindow):
    window.mdiArea.activeSubWindow().widget().undo()
