from PyQt6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont

class ResultWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget(3,3)
        font = QFont('Segoe UI', 11)
        self.table.setFont(font)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Result'))
        layout.addWidget(self.table)
        self.setLayout(layout)

    def clear_table(self, rows, cols):
        self.table.clear()
        self.table.setRowCount(rows); self.table.setColumnCount(cols)
        self.table.setHorizontalHeaderLabels([f"{i+1:d}" for i in range(cols)])
        self.table.setVerticalHeaderLabels([f"{i+1:d}" for i in range(rows)])

    def show_matrix(self, M):
        r = len(M); c = len(M[0]) if r>0 else 0
        self.clear_table(r,c)
        for i in range(r):
            for j in range(c):
                v = M[i][j]
                # display Fraction nicely
                try:
                    from fractions import Fraction
                    if isinstance(v, Fraction):
                        s = f"{v.numerator}/{v.denominator}" if v.denominator!=1 else str(v.numerator)
                    else:
                        s = str(v)
                except:
                    s = str(v)
                self.table.setItem(i,j, QTableWidgetItem(s))
