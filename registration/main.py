import json
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QLineEdit, 
    QPushButton,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QMessageBox
)
from PyQt5.QtGui import QFont
from additionals import *



class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Najot Talim")
        self.setGeometry(100, 100, 400, 500)
        self.setStyleSheet("background-color: #eee9e5; font-size: 20px;")
        
        self.v_box = QVBoxLayout()

#Title
        self.title = QLabel("Najot")
        self.title.setFont(QFont("Arial", 50, QFont.Bold))
        self.title.setStyleSheet("color: #1565C0;font-size: 30px") 

        self.subtitle = QLabel("chat")
        self.subtitle.setFont(QFont("Arial", 100, QFont.Bold))
        self.subtitle.setStyleSheet("color: #bc8e5b; font-size: 30px") 
        self.title_layout = QHBoxLayout()
        self.title_layout.addStretch()
        self.title_layout.addWidget(self.title)
        self.title_layout.addWidget(self.subtitle)
        self.title_layout.addStretch()

        self.v_box.addStretch()
        self.v_box.addLayout(self.title_layout)
        self.v_box.addStretch()

#Login
        self.login_edit = Edit()
        self.login_edit.setPlaceholderText("User Name:")

#Password
        self.pwd_edit = Edit()
        self.pwd_edit.setPlaceholderText("Password...")
        self.pwd_edit.setEchoMode(QLineEdit.Password)

        self.info_label = QLabel()
        self.info_label.setAlignment(Qt.AlignCenter)

        self.save_btn = Button("Login")
        self.register_button = Button("Create New Account")


#V_Box
        self.v_box2 = QVBoxLayout()
        self.v_box2.addWidget(self.login_edit)
        self.v_box2.addWidget(self.pwd_edit)
        self.v_box2.addWidget(self.info_label)
        self.v_box2.addWidget(self.save_btn)
        self.v_box2.addWidget(self.register_button)
        self.v_box2.setAlignment(Qt.AlignCenter)
        self.v_box.addLayout(self.v_box2)
        self.v_box.addStretch()

#Footer
        self.footer = QLabel("© 2024 Najot chat from Foundation N79")
        self.footer.setStyleSheet("font-family: Arial; font-size: 12px")
        self.footer.setAlignment(Qt.AlignCenter)
        self.v_box.addWidget(self.footer)

        self.setLayout(self.v_box)

        self.save_btn.clicked.connect(self.save_user)
        self.register_button.clicked.connect(self.open_registration_page) 


    def save_user(self):
        users = WriteJson.get_all_users()
        login = self.login_edit.text() 
        pwd = self.pwd_edit.text()

        if login and pwd:
            for user in users:
                if login == user['username'] and pwd == user['password']:
                    self.close()
                    self.welcome = Welcome(user)
                    self.welcome.show()
                    return
            else:
                self.info_label.setText("Please Create A New Account")
        else:
            self.info_label.setText("Login or password not entered")

    def open_registration_page(self):
        self.close()
        self.regist_page = Registration()
        self.regist_page.show()



class Welcome(QWidget):
    def __init__(self, user_info) -> None:
        super().__init__()
        self.user_info = user_info
        self.setWindowTitle('Welcome Page')
        self.setFixedSize(400, 600)
        self.setStyleSheet("font-size: 20px; background-color: #eee9e5;")
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.v_box = QVBoxLayout()

#Welcome
        self.label = QLabel(f"Welcome {(self.user_info['username']).capitalize()}")
        self.label.setFont(QFont("Arial", 50, QFont.Bold))
        self.label.setStyleSheet("color: #1565C0;font-size: 30px") 
        self.label.setAlignment(Qt.AlignCenter)

        self.info = QLabel("Your Information:\n")
        self.info.setAlignment(Qt.AlignCenter)

#Fullname
        self.fullname_label = QLabel(f"Fullname:")
        self.subname = QLabel(self.user_info['fullname'])
        self.fullname_label.setFont(QFont("Arial", 30, QFont.Bold))
        self.fullname_label.setStyleSheet("color: #bc8e5b;") 

        self.h_box1.addWidget(self.fullname_label)
        self.h_box1.addWidget(self.subname)
        self.h_box1.setAlignment(Qt.AlignLeft)
        

#Username
        self.user_label = QLabel(f"Username:")
        self.username = QLabel(self.user_info['username'])
        self.user_label.setFont(QFont("Arial", 30, QFont.Bold))
        self.user_label.setStyleSheet("color: #bc8e5b;") 


        self.h_box2.addWidget(self.user_label)
        self.h_box2.addWidget(self.username)
        self.h_box2.setAlignment(Qt.AlignLeft)

#V_Box
        self.v_box.addStretch()
        self.v_box.addWidget(self.label)
        self.v_box.addStretch()
        self.v_box.addWidget(self.info)
        # self.v_box.addStretch()

        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box1)
        self.v_box.addStretch()


        self.setLayout(self.v_box)

class WriteJson:
    @staticmethod
    def get_all_users():
        if not os.path.exists("users.json"):
            with open("users.json", "w") as file:
                json.dump([], file)
        
        with open("users.json", "r") as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                users = []
        return users

class Registration(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(100, 100, 400, 500)
        self.setStyleSheet("background-color: #eee9e5; font-size: 20px;")
        self.setWindowTitle("Registration Page")
        self.v_box = QVBoxLayout()
        
        self.signup = QLabel("Sign Up")
        self.signup.setFont(QFont("Arial", 100, QFont.Bold))
        self.signup.setStyleSheet("color: #1565C0; font-size: 30px; font-weight: bold")
        self.signup.setAlignment(Qt.AlignCenter)
#Email
        self.email_edit = Edit()
        self.email_edit.setPlaceholderText("Email:")   
        self.email_info  = QLabel()
        self.email_info.setStyleSheet("font-size: 12px; color: red;") 

#Fullname
        self.fullname_edit = Edit()
        self.fullname_edit.setPlaceholderText("Full Name:")
        self.fullname_info  = QLabel()
        self.fullname_info.setStyleSheet("font-size: 12px; color: red;") 

#Username
        self.username_edit = Edit()
        self.username_edit.setPlaceholderText("Username:")
        self.username_info  = QLabel()
        self.username_info.setStyleSheet("font-size: 12px; color: red;") 

#Password
        self.pwd_edit = Edit()
        self.pwd_edit.setPlaceholderText("Password:")
        self.pwd_edit.setEchoMode(QLineEdit.Password)
        self.pwd_info  = QLabel()
        self.pwd_info.setStyleSheet("font-size: 12px; color: red;") 

        self.signup_btn = Button("Sign Up")
        self.signup_btn.setFixedSize(200, 50)

#V_Box
        self.v_box.addStretch()
        self.v_box.addWidget(self.signup)
        self.v_box.addStretch()
        self.v_box.addWidget(self.email_edit)
        self.v_box.addWidget(self.email_info)

        self.v_box.addWidget(self.fullname_edit)
        self.v_box.addWidget(self.fullname_info)

        self.v_box.addWidget(self.username_edit)
        self.v_box.addWidget(self.username_info)

        self.v_box.addWidget(self.pwd_edit)
        self.v_box.addWidget(self.pwd_info)
        self.v_box.addStretch()
        self.v_box.addWidget(self.signup_btn,0,Qt.AlignCenter)
        self.v_box.addStretch()

        self.setLayout(self.v_box)

        self.signup_btn.clicked.connect(self.write_to_json)

#Backend
    def write_to_json(self):
        email = (self.email_edit.text()).lower()
        fullname = (self.fullname_edit.text()).lower()
        username = (self.username_edit.text()).lower()
        password = self.pwd_edit.text()

       
        email_valid = Check_User.check_email(email)
        password_valid = Check_User.check_password(password)
        username_valid = Check_User.check_username(username)

#Checking all information  
        if email_valid and password_valid and username_valid:
            user = {
                'email': email,
                'fullname': fullname,
                'username': username,
                'password': password
            }

            users = WriteJson.get_all_users()

            for info in users:
                if user["username"] == info["username"]:
                    self.username_info.setText("Username already exists!")
                    return

            users.append(user)
            with open("users.json", "w") as f2:
                json.dump(users, f2, indent=4)

            QMessageBox.information(self, "Success", "User Registered Successfully!")
            for widget in self.findChildren(QLineEdit):
                widget.clear()

            self.email_info.clear()
            self.pwd_info.clear()
            self.username_info.clear()
        else:
            if not email_valid:
                self.email_info.setText('Invalid Email')
                self.email_edit.clear()
            else:
                self.email_info.clear()

            if not password_valid:
                self.pwd_info.setText('Invalid Password')
                self.pwd_edit.clear()
            else:
                self.pwd_info.clear()

            if not username_valid:
                self.username_info.setText('Invalid Username')
                self.username_edit.clear()
            else:
                self.username_info.clear()

class Check_User:
    @staticmethod
    def check_email(email: str):
        email_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", 
                         "icloud.com", "aol.com", "protonmail.com", "zoho.com", 
                         "mail.com", "gmx.com", "yandex.com", "microsoft.com", 
                         "apple.com", "amazon.com", "ibm.com", "intel.com", "tesla.com", 
                         "harvard.edu", "stanford.edu", "mit.edu", "ox.ac.uk", "cam.ac.uk", 
                         "gov.uk", "gov.au", "gov.ca", "gov.in", "gov.us"]

        userdomain = email.split("@")[-1]
        return userdomain in email_domains
        
    @staticmethod
    def check_username(username: str):
        def check_punc(username: str):
            punctuation_string = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
            return all(char not in punctuation_string for char in username)

        return len(username) > 5 and check_punc(username) and ' ' not in username
        
    @staticmethod
    def check_password(password: str):
        punctuation_string = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

        def is_valid_password(password: str):
            has_upper = any(char.isupper() for char in password)
            has_lower = any(char.islower() for char in password)
            has_number = any(char.isdigit() for char in password)
            has_punc = any(char in punctuation_string for char in password)
            return has_upper and has_lower and has_number and has_punc

        return len(password) >= 8 and is_valid_password(password)

app = QApplication([])
win = Window()
win.show()
app.exec_()
