import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QMainWindow

class F(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setGeometry(100,100,600,300)
        self.setWindowTitle("Welcome Dear Alireza")
        self.btn = QPushButton("Close App", self)
        self.btn.move(300, 150)
        # btn.clicked.connect(self.click)
        # btn.clicked.connect(self.click2)
        self.btn.clicked.connect(self.exit)
        self.statusBar().showMessage("LOVE")
        self.show()

    def click(self):
        print("Hello World!")

    def click2(self):
        print("World is Beautiful!")

    def exit(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = F()
    sys.exit(app.exec_())