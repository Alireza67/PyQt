import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class test (QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setGeometry(100,100,600,400)
        self.setWindowTitle("TEST3")
        self.btn1 = QPushButton("Death", self)
        #self.btn1.setGeometry(200,200,90,40)
        self.btn1.move(200, 200)
        self.btn1.clicked.connect(self.closeApp)
        self.show()

    def closeApp(self):
        self.mess = QMessageBox.question(self,
                                         "Warning",
                                         "Do you want close the program?",
                                         QMessageBox.Yes,
                                         QMessageBox.No)
        if self.mess == QMessageBox.Yes:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex= test()
    sys.exit(app.exec_())
