# Automata Wordle UI
Automata Wordle is a simple, fun, and engaging word guessing game inspired by the popular online game Wordle. The game is built using Astro, a modern front-end framework for building fast, optimized web applications.  

## Features
- Guess a hidden word by typing letters.
- Each letter in the word is represented by a tile on the game board.
- The game provides feedback on your guesses:
  - Green: The letter is in the correct position.
  - Yellow: The letter is in the word but not in the correct position.
  - Gray: The letter is not in the word.
- The game ends when you have correctly guessed all the letters in the word or when you have exhausted all your attempts.

## Usage
> To play the game, is necessary to run both the backend and frontend services. See this [README](https://github.com/NastMz/Automata-Wordle/blob/main/README.md) for more details.

This project is used to build the frontend of the game. It provides a user interface for the game and communicates with the backend service to update the game state.
Is not necessary to run this project separately, it is already integrated with the backend service. However, if you want to run this project separately, you can do so by following these steps:

1. Install the dependencies:
   ```bash
   npm install
   ```
2. Start the development server:
   ```bash
    npm run dev
    ```
3. Open [http://localhost:4321](http://localhost:4321) with your browser to see the result.
4. Start the backend service by following the instructions in this [README](https://github.com/NastMz/Automata-Wordle/tree/main/backend/README.md) file.

## Additional Information

The generated files after a build have been copied to the backend service. This is done to simplify the deployment process. The backend service will serve the frontend files when the application is running. The files are copied to the `backend/static` directory. The `backend/static/index.html` file is renamed to `backend/templates/index.html` to allow Flask to render the file.
   
