import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout


class TestTables(QWidget):

    def __init__(self):
        super().__init__()
        self.TableLayout = QVBoxLayout()
        self.table1 = QTableWidget()
        self.set_ui()

    def set_ui(self):
        self.setGeometry(100, 100, 600, 300)
        self.setWindowTitle("Test Table")
        self.main_table()
        self.TableLayout.addWidget(self.table1)
        self.setLayout(self.TableLayout)
        self.show()

    def main_table(self):
        self.table1.setRowCount(4)
        self.table1.setColumnCount(3)
        self.table1.setItem(0, 1, QTableWidgetItem("Col 1"))
        self.table1.setItem(0, 2, QTableWidgetItem("COl 2"))
        self.table1.setItem(1, 0, QTableWidgetItem("Row 1"))
        self.table1.setItem(2, 0, QTableWidgetItem("Row 2"))
        self.table1.setItem(3, 0, QTableWidgetItem("Row 3"))
        self.table1.clicked.connect(self.print_cell)

    def print_cell(self):
        for cell in self.table1.selectedItems():
            print(cell.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TestTables()
    sys.exit(app.exec_())
