# Automata Wordle Desktop Application
Automata Wordle Desktop Application is a desktop version of the Automata Wordle game, a simple, fun, and engaging word guessing game inspired by the popular online game Wordle. This application is built using PySide6, a set of Python bindings for The Qt Company’s Qt application framework, and Flask, a lightweight and powerful web framework for Python.  

## Features
- Starts a Flask backend to serve the game mechanics as an API.
- Sets up a QWebEngineView to display the web content.
- Handles the application window events such as closing the window.

## Usage
> This project only contains the view layer of the application. To run the application, you need to run the application from the root directory.

Actually we don't provide a way to run this project separately. See this [README](https://github.com/NastMz/Automata-Wordle/tree/main/README.md) for more details about how to run the application.

## Additional Information

This project is used to provide the possibility to run the game simulating a desktop application instead of running it in the browser. But, the entire game is implemented in the backend service and can be deployed as a web application. For more details about the backend service, please refer to this [README](https://github.com/NastMz/Automata-Wordle/tree/main/backend/README.md)