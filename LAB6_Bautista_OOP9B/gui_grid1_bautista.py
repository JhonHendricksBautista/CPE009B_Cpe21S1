import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt Login Screen"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))
        self.createGridLayout()
        self.setLayout(self.layout)
        self.show()

    def createGridLayout(self):
        self.layout = QGridLayout()
        self.layout.setColumnStretch(1, 2)

        self.textboxlbl = QLabel("Username:", self)
        self.textbox = QLineEdit(self)

        self.passwordlbl = QLabel("Password:", self)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)

        self.button = QPushButton('Register', self)
        self.button.setToolTip("You've hovered over me!")

        self.layout.addWidget(self.textboxlbl, 0, 0)
        self.layout.addWidget(self.textbox, 0, 1)
        self.layout.addWidget(self.passwordlbl, 1, 0)
        self.layout.addWidget(self.password, 1, 1)
        self.layout.addWidget(self.button, 2, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
