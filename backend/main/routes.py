from .blueprints import main
from flask import send_from_directory


@main.route('/')
def home():
    return send_from_directory('templates', 'index.html')
