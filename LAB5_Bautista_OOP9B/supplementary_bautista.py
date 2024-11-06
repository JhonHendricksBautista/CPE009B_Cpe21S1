import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
import csv

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Account Registration")
        self.setGeometry(200, 200, 360, 300)
        self.initUI()

    def initUI(self):
        font = QFont()
        font.setPointSize(12)  

        self.first_name_label = QLabel("First Name:", self)
        self.first_name_label.setFont(font)
        self.first_name_label.move(20, 20)

        self.last_name_label = QLabel("Last Name:", self)
        self.last_name_label.setFont(font)
        self.last_name_label.move(20, 60)

        self.username_label = QLabel("Username:", self)
        self.username_label.setFont(font)
        self.username_label.move(20, 100)

        self.password_label = QLabel("Password:", self)
        self.password_label.setFont(font)
        self.password_label.move(20, 140)

        self.email_label = QLabel("Email Address:", self)
        self.email_label.setFont(font)
        self.email_label.move(20, 180)

        self.contact_label = QLabel("Contact No.:", self)
        self.contact_label.setFont(font)
        self.contact_label.move(20, 220)


        self.first_name_input = QLineEdit(self)
        self.first_name_input.setFont(font)
        self.first_name_input.move(140, 20)
        self.first_name_input.resize(180, 30)

        self.last_name_input = QLineEdit(self)
        self.last_name_input.setFont(font)
        self.last_name_input.move(140, 60)
        self.last_name_input.resize(180, 30)

        self.username_input = QLineEdit(self)
        self.username_input.setFont(font)
        self.username_input.move(140, 100)
        self.username_input.resize(180, 30)

        self.password_input = QLineEdit(self)
        self.password_input.setFont(font)
        self.password_input.move(140, 140)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.resize(180, 30)

        self.email_input = QLineEdit(self)
        self.email_input.setFont(font)
        self.email_input.move(140, 180)
        self.email_input.resize(180, 30)

        self.contact_input = QLineEdit(self)
        self.contact_input.setFont(font)
        self.contact_input.move(140, 220)
        self.contact_input.resize(180, 30)

        # Buttons
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setFont(font)
        self.submit_button.move(80, 260)
        self.submit_button.clicked.connect(self.register_account)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.setFont(font)
        self.clear_button.move(180, 260)
        self.clear_button.clicked.connect(self.clear_all)

        self.show()

    def clear_all(self):
        self.first_name_input.clear()
        self.last_name_input.clear()
        self.username_input.clear()
        self.password_input.clear()
        self.email_input.clear()
        self.contact_input.clear()

    @pyqtSlot()
    def register_account(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        email = self.email_input.text()
        contact = self.contact_input.text()

        if not all([first_name, last_name, username, password, email, contact]):
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return
        
        try:
            with open("accounts.csv", "a", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([first_name, last_name, username, password, email, contact])
            QMessageBox.information(self, "Success", "Account successfully registered!")
            self.clear_all()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Registration failed: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationForm()
    sys.exit(app.exec_())
