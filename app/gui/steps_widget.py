from PyQt6.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont

class StepsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.editor = QTextEdit()
        self.editor.setReadOnly(True)
        self.editor.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        font = QFont('Consolas', 10)
        self.editor.setFont(font)
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Steps'))
        layout.addWidget(self.editor)
        self.setLayout(layout)

    def set_steps(self, steps_list):
        if not steps_list:
            self.editor.setPlainText('No steps available')
            return
        self.editor.setPlainText('\n\n'.join(steps_list))

    def clear(self):
        self.editor.clear()
