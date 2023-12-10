from .blueprints import main
from flask import render_template


@main.route('/')
def home():
    return render_template('index.html')