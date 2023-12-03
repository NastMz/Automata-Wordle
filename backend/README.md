# Automata Wordle API
Automata Wordle API is a backend service built with Flask, a lightweight and powerful web framework for Python. This API serves the game mechanics for the Automata Wordle game, a simple, fun, and engaging word guessing game inspired by the popular online game Wordle.  

## Features
- Provides endpoints for game initialization, letter guessing, and game status checking.
- Handles game logic such as validating guesses, providing feedback, and determining game over conditions.
- Serves static files for the frontend application.

## Usage
1. Send a GET request to `/start` to initialize a new game.
2. Send a POST request to `/guess` with a letter to make a guess.
3. Send a GET request to `/status` to get the current game status.

## API Endpoints
- `GET /start`: Initializes a new game and returns the initial game state.
- `POST /guess`: Accepts a letter as input and returns the updated game state.
- `GET /status`: Returns the current game state.

## Playing the Game
The backend service already comes integrated with the frontend service. To play the game, you only need to run the backend service. To run the backend service, follow these steps:

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
2. Start the backend service:
   ```bash
    python backend/app.py
    ```
   
3. Open [http://localhost:5000](http://localhost:5000) with your browser to see the result.

## Additional Information

However, while you can run the backend service and play the game, it is recommended to run the desktop application instead. The desktop application starts the backend service and sets up a QWebEngineView to display the web content. It also handles the application window events such as closing the window. For more details about the desktop application, please refer to this [README](https://github.com/NastMz/Automata-Wordle/tree/main/README.md) file.