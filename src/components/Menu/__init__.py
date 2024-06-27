import PySide6.QtCore
from PySide6.QtWidgets import QMenu, QMainWindow
from PySide6.QtGui import QAction


class MenuBar(Qmenu):
    def __init__(self) -> None:
        super().__init__()

    #& 파일 탭 
    def get_menu(self):
        mFile = QMenu('파일', self)
        
        #^ 파일 열기 
        c_open_file = QAction("파일 열기", self)
        c_open_file.setShortcut("Ctrl+O")
        c_open_file.triggered.connect(self.close)

        c_close = QAction("종료하기", self)
        c_close.setShortcut("Ctrl+W")
        c_close.triggered.connect(self.close)

        mFile.addAction(c_open_file)
        mFile.addAction(c_close)
        return mFile

