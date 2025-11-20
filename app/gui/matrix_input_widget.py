from PyQt6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class MatrixInputWidget(QWidget):
    def __init__(self, rows=3, cols=3):
        super().__init__()
        self.table = QTableWidget(rows, cols)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

        self.setup_table(rows, cols)

    def setup_table(self, rows, cols):
        self.table.clear()
        self.table.setRowCount(rows)
        self.table.setColumnCount(cols)

        self.table.setHorizontalHeaderLabels([f"{i+1:d}" for i in range(cols)])
        self.table.setVerticalHeaderLabels([f"{i+1:d}" for i in range(rows)])

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        font = QFont('Segoe UI', 11)
        self.table.setFont(font)

        # prefill editable entries
        for i in range(rows):
            for j in range(cols):
                item = QTableWidgetItem("0")
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(i, j, item)

    def fill_sample(self):
        counter = 1
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                item = QTableWidgetItem(str(counter))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(i, j, item)
                counter += 1

