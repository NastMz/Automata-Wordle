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