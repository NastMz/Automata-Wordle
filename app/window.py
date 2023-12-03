import subprocess

from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow

from app.config import APP_CONFIG


class AppWindow(QMainWindow):
    """
    This class represents the main application window. It inherits from QMainWindow.
    It starts a Flask backend on initialization and sets up a QWebEngineView to display the web content.
    """

    def __init__(self):
        """
        Constructor for the AppWindow class. Initializes the Flask backend and the QWebEngineView.
        """
        super(AppWindow, self).__init__()

        self.flask_process = None
        self.start_flask_backend()

        self.browser = QWebEngineView()
        url = QUrl(f"http://{APP_CONFIG['host']}:{APP_CONFIG['port']}")  # Create a URL object
        self.browser.setUrl(url)  # Set the URL of the web content to be displayed
        self.setCentralWidget(self.browser)  # Set the browser as the central widget of the window
        self.showMaximized()  # Show the window maximized
        self.setWindowTitle("Automata Wordle")  # Set the window title
        self.setWindowIcon(QIcon('assets/icon.png'))  # Set the window icon

    def start_flask_backend(self):
        """
        Starts the Flask backend by running a Python script using subprocess.
        """
        python_executable = 'python'
        script_path = 'backend/app.py'

        self.flask_process = subprocess.Popen([python_executable, script_path], shell=True, stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)

    def closeEvent(self, event):
        """
        Overrides the closeEvent method from QMainWindow.
        Terminates the Flask backend process when the window is closed.
        """
        if self.flask_process:
            self.flask_process.terminate()  # Terminate the Flask process
            self.flask_process.wait(1)  # Wait for the process to terminate

            if self.flask_process.poll() is None:  # If the process is still running
                self.flask_process.kill()  # Kill the process

        event.accept()  # Accept the close event
