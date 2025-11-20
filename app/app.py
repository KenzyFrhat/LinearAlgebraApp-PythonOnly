import sys
from PyQt6.QtWidgets import QApplication
from app.gui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(900,600)
    w.show()
    sys.exit(app.exec())
