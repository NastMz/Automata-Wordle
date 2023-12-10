from backend.app import socketio
from flask_socketio import emit
from ..core.automata import Automata

automata = Automata()


@socketio.on('start', namespace='/game')
def handle_start_game(msg):
    """
     Initiates the game when the 'start' event is received.

    This function is triggered when a 'start' event is received through the '/game' namespace.
    It calls the 'update' method of the Automata class with the 'start' symbol,
    initiates the game, and emits the result to the connected client.

    Args:
        msg (dict): The message received from the client, not used in this function.

    Emits:
        'start' event: The result of the 'update' method, containing game information.
    """
    result = automata.update('start')
    emit('start', result)


@socketio.on('escribir', namespace='/game')
def handle_write(msg):
    """
     Handles the player's input when the 'escribir' event is received.

    This function is triggered when an 'escribir' event is received through the '/game' namespace.
    It calls the 'update' method of the Automata class with the 'escribir' symbol and the written word,
    updates the game state, and emits the result to the connected client.

    Args:
        msg (dict): The message received from the client, containing the written word.

    Emits:
        'escribir' event: The result of the 'update' method, containing game information.
    """
    result = automata.update('escribir', msg['word'])
    emit('escribir', result)


@socketio.on('verificar', namespace='/game')
def handle_verify(msg):
    """
    Handles the verification process when the 'verificar' event is received.

    This function is triggered when a 'verificar' event is received through the '/game' namespace.
    It calls the 'update' method of the Automata class with the 'verificar' symbol,
    performs the verification process, and emits the result to the connected client.

    Args:
        msg (dict): The message received from the client, not used in this function.

    Emits:
        'verificar' event: The result of the 'update' method, containing game information.
    """
    result = automata.update('verificar')
    emit('verificar', result)
