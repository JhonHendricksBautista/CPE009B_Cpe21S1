import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()  # initializes the main window
        self.title = "First OOP GUI"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(200, 200, 300, 300)
        self.setWindowIcon(QIcon('crown.ico'))  # sets an icon
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = App()
    sys.exit(app.exec())
