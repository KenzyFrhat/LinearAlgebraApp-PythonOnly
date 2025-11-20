from PyQt6.QtWidgets import (
    QWidget, QLabel, QSpinBox, QPushButton, QVBoxLayout, QHBoxLayout,
    QSizePolicy, QStyle, QMessageBox
)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt
from app.gui.matrix_input_widget import MatrixInputWidget
from app.gui.result_widget import ResultWidget
from app.gui.steps_widget import StepsWidget
from app.core.ref import ref_with_steps
from app.core.rref import rref_with_steps
from app.core.transpose import transpose_matrix
from app.core.inverse import inverse_with_steps
from app.utils.matrix_parser import parse_matrix_from_table
from fractions import Fraction

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Linear Algebra App — REF / RREF / Transpose / Inverse')
        self.init_ui()

    def init_ui(self):
        font = QFont('Segoe UI', 10)
        self.setFont(font)
        # Top controls: rows, cols, generate
        top_layout = QHBoxLayout()
        top_layout.addWidget(QLabel('Rows:'))
        self.spin_rows = QSpinBox(); self.spin_rows.setRange(1, 12); self.spin_rows.setValue(3)
        top_layout.addWidget(self.spin_rows)
        top_layout.addWidget(QLabel('Cols:'))
        self.spin_cols = QSpinBox(); self.spin_cols.setRange(1, 12); self.spin_cols.setValue(3)
        top_layout.addWidget(self.spin_cols)
        self.btn_generate = QPushButton('Create Matrix')
        self.btn_generate.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogNewFolder))
        top_layout.addWidget(self.btn_generate)

        # Matrix input widget
        self.matrix_widget = MatrixInputWidget(3,3)
        self.matrix_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Buttons
        btn_layout = QHBoxLayout()
        self.btn_ref = QPushButton('REF'); self.btn_rref = QPushButton('RREF')
        self.btn_transpose = QPushButton('Transpose'); self.btn_inverse = QPushButton('Inverse')
        for b in (self.btn_ref, self.btn_rref, self.btn_transpose, self.btn_inverse):
            b.setMinimumHeight(36)
            btn_layout.addWidget(b)

        # Result and steps widgets
        self.result_widget = ResultWidget()
        self.steps_widget = StepsWidget()

        # Arrange main layout
        main = QVBoxLayout()
        main.addLayout(top_layout)
        main.addWidget(self.matrix_widget, 1)
        main.addLayout(btn_layout)
        bottom = QHBoxLayout()
        bottom.addWidget(self.result_widget, 1)
        bottom.addWidget(self.steps_widget, 1)
        main.addLayout(bottom, 2)
        self.setLayout(main)

        # Connections
        self.btn_generate.clicked.connect(self.create_table)
        self.btn_ref.clicked.connect(self.do_ref)
        self.btn_rref.clicked.connect(self.do_rref)
        self.btn_transpose.clicked.connect(self.do_transpose)
        self.btn_inverse.clicked.connect(self.do_inverse)

        # sample values
        self.matrix_widget.fill_sample()

    def create_table(self):
        r = self.spin_rows.value(); c = self.spin_cols.value()
        self.matrix_widget.setup_table(r,c)
        self.result_widget.clear_table(r,c)
        self.steps_widget.clear()

    def do_ref(self):
        try:
            A = parse_matrix_from_table(self.matrix_widget.table)
            R, steps = ref_with_steps(A)
            self.result_widget.show_matrix(R)
            self.steps_widget.set_steps(steps)
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))

    def do_rref(self):
        try:
            A = parse_matrix_from_table(self.matrix_widget.table)
            R, steps = rref_with_steps(A)
            self.result_widget.show_matrix(R)
            self.steps_widget.set_steps(steps)
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))

    def do_transpose(self):
        try:
            A = parse_matrix_from_table(self.matrix_widget.table)
            T = transpose_matrix(A)
            self.result_widget.show_matrix(T)
            self.steps_widget.set_steps(['Transpose performed'])
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))

    def do_inverse(self):
        try:
            A = parse_matrix_from_table(self.matrix_widget.table)
            Inv, steps = inverse_with_steps(A)
            self.result_widget.show_matrix(Inv)
            self.steps_widget.set_steps(steps if steps else ['Inverse computed'])
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))
