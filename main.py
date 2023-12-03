import sys

from PySide6.QtWidgets import QApplication
from app.window import AppWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec())
