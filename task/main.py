
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QLineEdit)

contact_info = []

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()


        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Contact Manager")
        self.h_box = QHBoxLayout()
        self.v_box = QVBoxLayout()

        self.add_contact = QPushButton("Add Contact")
        self.edit_contact = QPushButton("Edit Contact")
        self.delete_contact = QPushButton("Delete Contact")
        
        self.h_box.addWidget(self.add_contact)
        self.h_box.addWidget(self.edit_contact)
        self.h_box.addWidget(self.delete_contact)

        self.contact_list = QListWidget()
        self.v_box.addWidget(self.contact_list)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

        self.add_contact.clicked.connect(self.add_contacts)
        self.edit_contact.clicked.connect(self.edit_contacts)
    
    def add_contacts(self):
        self.addwindow = Add_Contact_WIndow(self.contact_list)
    
    def edit_contacts(self):
        self.editwindow = Edit_Window()


        

class Add_Contact_WIndow(QWidget):
    def __init__(self,contact_list) -> None:
        super().__init__()
        self.contact_list = contact_list

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Add Contact")
        self.v_box = QVBoxLayout()

        self.name = QLabel("Name:")
        self.phone = QLabel("Phone:")
        self.email = QLabel("Email:")
        self.save_button = QPushButton("Save")

        self.name_edit = QLineEdit()
        self.phone_edit = QLineEdit()
        self.email_edit = QLineEdit()
        

        self.v_box.addWidget(self.name)
        self.v_box.addWidget(self.name_edit)
        self.v_box.addWidget(self.phone)
        self.v_box.addWidget(self.phone_edit)
        self.v_box.addWidget(self.email)
        self.v_box.addWidget(self.email_edit)
        self.v_box.addWidget(self.save_button)

        self.setLayout(self.v_box)

        self.save_button.clicked.connect(self.save_contact)

        self.show()

    def save_contact(self):
        name = self.name_edit.text()
        phone = self.phone_edit.text()
        email = self.email_edit.text()

        contact = {
            "name" : name,
            "phone" : phone,
            "email" : email
        }
        self.contact_list.addItem(name)
        contact_info.append(contact)

        for widget in self.findChildren(QLineEdit):
            widget.clear()
        

class Edit_Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Edit Contact")
        self.v_box = QVBoxLayout()

        self.name = QLabel("Name:")
        self.phone = QLabel("Phone:")
        self.email = QLabel("Email:")
        self.save_button = QPushButton("Save")

        self.name_edit = QLineEdit()
        self.phone_edit = QLineEdit()
        self.email_edit = QLineEdit()
        

        self.v_box.addWidget(self.name)
        self.v_box.addWidget(self.name_edit)
        self.v_box.addWidget(self.phone)
        self.v_box.addWidget(self.phone_edit)
        self.v_box.addWidget(self.email)
        self.v_box.addWidget(self.email_edit)
        self.v_box.addWidget(self.save_button)

        self.setLayout(self.v_box)

        new_name = self.name_edit.text()
        new_phone = self.phone_edit.text()
        new_email = self.email_edit.text()

        self.show()


app = QApplication([])
win = Window()
win.show()
app.exec_()













