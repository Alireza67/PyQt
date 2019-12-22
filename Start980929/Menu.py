import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

class testMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setGeometry(100,100,600,300)
        self.setWindowTitle("Test Menu")
        self.mainMenu = self.menuBar()
        self.mFile= self.mainMenu.addMenu("File")
        self.mEdit = self.mainMenu.addMenu("Edit")
        self.newB = QAction("New", self)
        self.exitB = QAction("Exit", self)
        self.mFile.addAction(self.newB)
        self.mFile.addAction(self.exitB)
        self.exitB.triggered.connect(self.exitApp)
        self.show()

    def exitApp(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = testMenu()
    sys.exit(app.exec_())