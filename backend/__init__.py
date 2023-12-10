from flask import Flask
from .main.blueprints import main as main_blueprint
from .main.websocket import socketio


def create_app(debug=False):
    """
    Create and configure the Flask application.

    This function creates a Flask application, configures it, registers blueprints,
    and initializes the Socket.IO extension.

    Args:
        debug (bool): Enable or disable debug mode. Default is False.

    Returns:
        Flask: The configured Flask application.

    Configuration:
        - SECRET_KEY (str): A secret key for securing the application.

    Blueprints:
        - 'main': The main blueprint containing routes and views.

    Socket.IO:
        The Socket.IO extension is initialized for handling real-time communication.
    """
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app
