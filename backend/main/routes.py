from . import main
from flask import render_template


@main.route('/')
def home():
    """
    Doc here
    """
    return render_template('index.html')