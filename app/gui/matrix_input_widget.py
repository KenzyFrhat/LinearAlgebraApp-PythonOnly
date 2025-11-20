from PyQt6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QFont, QIntValidator
from PyQt6.QtCore import Qt

class MatrixInputWidget(QWidget):
    def __init__(self, rows=3, cols=3):
        super().__init__()
        self.table = QTableWidget(rows, cols)
        self.setup_table(rows, cols)

    def setup_table(self, rows, cols):
        self.table.clear()
        self.table.setRowCount(rows)
        self.table.setColumnCount(cols)
        self.table.setHorizontalHeaderLabels([str(i+1) for i in range(cols)])
        self.table.setVerticalHeaderLabels([str(i+1) for i in range(rows)])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        font = QFont('Segoe UI', 11)
        self.table.setFont(font)
        # pre-fill empty items for better UX
        for i in range(rows):
            for j in range(cols):
                self.table.setItem(i, j, QTableWidgetItem('0'))

    def fill_sample(self):
        samples = [['1','2','3'],['4','5','6'],['7','8','9']]
        r = min(self.table.rowCount(), 3)
        c = min(self.table.columnCount(), 3)
        for i in range(r):
            for j in range(c):
                self.table.setItem(i,j, QTableWidgetItem(samples[i][j]))
