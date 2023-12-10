from flask import Flask
from .main.blueprints import main as main_blueprint
from .main.websocket import socketio


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app
