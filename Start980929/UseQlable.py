import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QLabel, QPushButton, QAction


class UseQLabel(QMainWindow):

    def __init__(self):
        super().__init__()
        self.line1 = QLineEdit(self)
        self.line2 = QLineEdit(self)
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.btnCopy = QPushButton(self)
        self.btnCopy.clicked.connect(self.copy_function)
        self.menu1 = self.menuBar()
        self.set_ui()

    def set_ui(self):
        self.setGeometry(100, 100, 600, 300)
        self.line1.setGeometry(85, 45, 200, 20)
        self.line2.setGeometry(85, 75, 200, 20)
        self.btnCopy.move(130, 105)
        self.label1.move(35, 45)
        self.label2.move(35, 75)
        self.setWindowTitle("QLabel")
        self.label1.setText("Input: ")
        self.label2.setText("OutPut: ")
        self.btnCopy.setText("Copy")

        file_m = self.menu1.addMenu("File")
        edit_m = self.menu1.addMenu("Edit")

        sub_menu_close = QAction("Close", self)
        sub_menu_delete = QAction("Delete", self)

        file_m.addAction(sub_menu_close)
        edit_m.addAction(sub_menu_delete)
        
        sub_menu_close.triggered.connect(self.close_app)
        sub_menu_delete.triggered.connect(self.del_text)

        self.show()

    def copy_function(self):
        temp = self.line1.text()
        self.line2.setText(temp)

    def close_app(self):
        self.close()

    def del_text(self):
        self.line1.setText("")
        self.line2.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = UseQLabel()
    sys.exit(app.exec_())
