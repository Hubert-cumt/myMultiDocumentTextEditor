import webbrowser
from MainWindows import MainWindow


# 本文件是关于功能实现

def func_about():
    try:
        webbrowser.get('chrome').open_new_tab('https://github.com/Hubert-cumt/myMultiDocumentTextEditor')
    except Exception as e:
        webbrowser.open_new_tab('https://github.com/Hubert-cumt/myMultiDocumentTextEditor')
