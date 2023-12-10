import sys

from PySide6.QtWidgets import QApplication
from app.window import AppWindow

def start_app():
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    start_app()
