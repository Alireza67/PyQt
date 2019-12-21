import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton

class useLIneEdit(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setGeometry(100,100,250,150)
        self.setWindowTitle("Line Edit")
        self.textLine1 = QLineEdit(self)
        self.textLine2 = QLineEdit(self)
        self.textLine1.move(20,20)
        self.textLine2.move(20,50)
        self.textLine1.resize(200,20)
        self.textLine2.resize(200,20)
        self.btn = QPushButton("Copy", self)
        self.btn.clicked.connect(self.copy)
        self.btn.move(50, 100)
        self.show()

    def copy(self):
        content = self.textLine1.text()
        self.textLine2.setText(content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = useLIneEdit()
    sys.exit(app.exec_())