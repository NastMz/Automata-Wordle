# Automata Wordle API
Automata Wordle API is a backend service built with Flask, a lightweight and powerful web framework for Python. This API serves the game mechanics for the Automata Wordle game, a simple, fun, and engaging word guessing game inspired by the popular online game Wordle.  

## Features
- The game logic is managed by the provided Automata class, and the application utilizes Flask-SocketIO for real-time communication between the server and clients.
- Handles game logic such as validating guesses, providing feedback, and determining game over conditions.
- Serves static files for the frontend application.

## Project Structure

```
Automata-Wordle/
│
├── backend/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── constants.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── automata.py
│   │   ├── utils.py
│   │   └── words.txt
│   ├── core/
│   │   ├── __init__.py
│   │   ├── events.py
│   │   └── routes.txt
│   ├── static/
│   │   ├── favicon.svg
│   │   └── index.css
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│   ├── README.md
├── README.md
├── requirements.txt
└── ...
```

## Usage
- Access the application at `http://localhost:5000`.
- Follow the on-screen instructions to play the word-guessing game.
- WebSocket events (`start`, `escribir`, `verificar`) are handled through the `/game` namespace.

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
