from .blueprints import main
from flask import send_from_directory


@main.route('/')
def home():
    """
    Renders the home page.

    This route is associated with the root path ('/'). When a request is made to the root path,
    this function is called, and it renders the 'index.html' template using Flask's 'render_template' function.

    Returns:
        str: The rendered HTML content of the 'index.html' template
    """
    return send_from_directory('templates', 'index.html')
