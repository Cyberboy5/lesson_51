
from PyQt5.QtWidgets import QLineEdit,QPushButton


class Edit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            border: 2px solid #9E9E9E;
            border-radius: 10px;
            padding: 10px;
            font-size: 14px;
        """)

class Button(QPushButton):
    def __init__(self, text=""):
        super().__init__(text)
        self.setStyleSheet("""
        QPushButton {
            border: none;
            border-radius: 10px;
            padding: 10px;
            background-color: #bc8e5b;
            color: white;                               
        }
        QPushButton:hover {
            border: 2px solid #e0a309;
            background-color: #ffffff;
            color: black
        }
        """)
