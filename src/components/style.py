from typing import Any
from PySide6.QtWidgets import QLabel

class style_sheet():
    def __init__(self) -> None:
        self.default()
    def default(self, *args: Any, **kwds: Any) -> Any:
        style ="""
            QWidget{
                border: 1px solid grey;
            }
        """
        return style
    
class H1(QLabel):
    def __init__(self, text:str = ''):
        super().__init__(text)
        super().setStyleSheet("color: grey;")
