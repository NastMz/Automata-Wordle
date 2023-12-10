import runpy
import subprocess
import sys
import time
import requests

from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow

from app.config import APP_CONFIG


class AppWindow(QMainWindow):
    """
    This class represents the main application window. It inherits from QMainWindow.
    It sets up a QWebEngineView to display the web content.
    """

    def __init__(self):
        """
        Constructor for the AppWindow class. Initializes the QWebEngineView.
        """
        super(AppWindow, self).__init__()

        self.flask_process = subprocess.Popen([sys.executable, 'backend/app.py'], stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)

        # Wait for the server to start
        while not self.is_server_running(APP_CONFIG['host'], APP_CONFIG['port']):
            time.sleep(1)

        self.browser = QWebEngineView()
        url = QUrl(f"http://{APP_CONFIG['host']}:{APP_CONFIG['port']}")  # Create a URL object
        self.browser.setUrl(url)  # Set the URL of the web content to be displayed
        self.setCentralWidget(self.browser)  # Set the browser as the central widget of the window
        self.showMaximized()  # Show the window maximized
        self.setWindowTitle("Automata Wordle")  # Set the window title
        self.setWindowIcon(QIcon('assets/icon.png'))  # Set the window icon

        # Focus the window
        self.activateWindow()

    @staticmethod
    def is_server_running(host, port):
        try:
            response = requests.get(f'http://{host}:{port}')
            return response.status_code == 200
        except:
            return False

    def closeEvent(self, event):
        """
        This method is called when the window is closed.

        """

        # Terminate the Flask process
        self.flask_process.terminate()
        self.flask_process.wait()

        if self.flask_process is not None:
            self.flask_process.kill()

        event.accept()


def run_flask():
    """
    Runs the Flask backend using subprocess.
    """
    script_path = 'backend/app.py'
    runpy.run_path(script_path, run_name="__main__")
