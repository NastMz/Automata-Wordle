# Automata Wordle

Automata Wordle is a fun and engaging word guessing game inspired by the popular online game Wordle. The game is built using a combination of technologies including Python, Flask, PySide6, TypeScript, JavaScript, and npm. It implements the game mechanics using DFA, a formal model of computation that describes how an automaton responds to a sequence of inputs. The game is designed to be played on a desktop computer.

## Features

- A Flask backend that serves the game mechanics as an API.
- A PySide6 desktop application that starts the Flask backend and sets up a QWebEngineView to display the web content.
- A frontend built using Astro, a modern front-end framework for building fast, optimized web applications.
- Game logic such as validating guesses, providing feedback, and determining game over conditions.

## Usage

To play the game, both the backend and frontend services need to be running (See [Running the Application](#running-the-application)). Once the application is running, you can start guessing letters. The game will provide feedback on your guesses and update the game board accordingly. Continue guessing letters until you have correctly guessed the word or exhausted all your attempts.

## Structure

The project is divided into three main parts:

- `app`: This directory contains the PySide6 desktop application. It starts a Flask backend and sets up a QWebEngineView to display the web content. It also handles the application window events such as closing the window.

- `backend`: This directory contains the Flask backend service. It provides endpoints for game initialization, letter guessing, and game status checking. It also handles game logic and serves static files for the frontend application.

- `ui`: This directory contains the frontend of the game built using Astro. It provides a user interface for the game and communicates with the backend service to update the game state.

For more details about each part, please refer to the README files in the respective directories.

## Running the Application

To run the application, you only need to run the `main.py` file in the root directory. This will start the backend service and open the desktop application window. The application window will display the game board and a virtual keyboard. You can use the virtual keyboard or use your physical keyboard to type letters and submit your guesses. The game board will update to reflect your guesses. Continue guessing letters until you have correctly guessed the word or exhausted all your attempts.

Follow these steps to run the application:

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
    python main.py
    ```
   