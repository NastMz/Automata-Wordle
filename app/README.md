# Automata Wordle Desktop Application
Automata Wordle Desktop Application is a desktop version of the Automata Wordle game, a simple, fun, and engaging word guessing game inspired by the popular online game Wordle. This application is built using PySide6, a set of Python bindings for The Qt Company’s Qt application framework, and Flask, a lightweight and powerful web framework for Python.  

## Features
- Starts a Flask backend to serve the game mechanics as an API.
- Sets up a QWebEngineView to display the web content.
- Handles the application window events such as closing the window.

## Usage
- The application starts with an empty game board.
- Type a letter and press Enter to submit your guess.
- The game board will update to reflect your guess.
- Continue guessing letters until you have correctly guessed the word or exhausted all your attempts.