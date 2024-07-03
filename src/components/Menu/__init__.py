from PySide6.QtWidgets import QMenu, QMenuBar, QApplication
from PySide6.QtGui import QAction


class MenuBar(QMenuBar):
    def __init__(self) -> None:
        super().__init__()
        self.init_menu()

    ## 메뉴 전체 
    def init_menu(self):
        self.init_app()
        self.init_file()
    
    ## 앱 메뉴
    def init_app(self):
        menu = QMenu('텍스트 분석보드', self)
        #^ 도움말 
        menu_help = QAction("도움말", self)
        menu_help.setShortcut("Alt+H")

        #^ 종료하기 
        menu_quit = QAction("종료하기", self)
        menu_quit.setShortcut("Ctrl+Q")
        menu_quit.triggered.connect(QApplication.instance().quit)

        menu.addAction(menu_help)
        menu.addSeparator()
        menu.addAction(menu_quit)
        #* 
        #* 프로그램 정보
        #* 
        #* 
        #* 기본설정 
        #* 종료하기
        self.addMenu(menu)
        
    ## 파일 메뉴
    def init_file(self):
        menu = QMenu('파일', self)
        
        #^ 파일 열기 
        c_open_file = QAction("파일 열기", self)
        c_open_file.triggered.connect(self.close)
        
        menu.addAction(c_open_file)
        menu.addSeparator()

        #* 파일 열기 
        #* 파일 초기화
        self.addMenu(menu)

