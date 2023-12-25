from PyQt5.QtGui import QTextCursor, QPalette

from MainWindows import MainWindow


# 本文件是搜索相关功能实现
# 搜索功能还在debug 12/ 25

def func_search(window: MainWindow):
    if window.empty():
        return
    sub = window.mdiArea.activeSubWindow().widget()
    sub.moveCursor(QTextCursor.Start)
    window.count = -1
    window.SearchBox.show()


def search_word(window: MainWindow):
    pattern = window.SearchBox.keyword_line.text()
    if pattern == "":
        return;
    sub = window.mdiArea.activeSubWindow().widget()

    if sub.find(pattern):
        # 找到标记
        window.sw_work = True
        # 测试
        window.count = window.count + 1

        print("self.count", window.count)
        palette = sub.palette()
        palette.setColor(QPalette.Highlight, palette.color(QPalette.Active, QPalette.Highlight))
        sub.setPalette(palette)
    else:
        sub.moveCursor(QTextCursor.Start)
        window.count = -1
        if sub.find(pattern):
            window.count = window.count + 1
            window.sw_work = True
            palette = sub.palette()
            palette.setColor(QPalette.Highlight, palette.color(QPalette.Active, QPalette.Highlight))
            sub.setPalette(palette)
        print("self.count", window.count)
    print("search_word self.count:", window.count)


def replace_word(window: MainWindow):
    # 确保被选中才能执行replace_word
    if not window.sw_work:
        return
    else:
        window.sw_work = False

    pattern = window.SearchBox.keyword_line.text()
    sub = window.mdiArea.activeSubWindow().widget()

    tar = window.SearchBox.replace_line.text()
    text = sub.toPlainText()
    # 待替换关键词的长度
    l = len(pattern)

    # 开始搜索的索引
    start = 0
    backup = window.count

    while backup:
        print("循环里backup :", backup)
        idx = text.find(pattern, start)
        print("循环里idx :", idx)
        start = (idx + l)
        backup = backup - 1
    idx = text.find(pattern, start)
    print("出来时start：", start)
    print("出来时：", backup)
    print("idx:", idx)
    h = text[0:idx]
    t = text[idx + l:]
    print("关键字长度：", l)
    print("前缀：", h)
    print("后缀：", t)
    print("self.count:", window.count)
    text = h + tar + t
    sub.setText(text)

    window.count -= 1
    bk = window.count
    sub.moveCursor(QTextCursor.Start)
    while bk != -1:
        window.sw_work = True
        bk -= 1
        sub.find(pattern)
