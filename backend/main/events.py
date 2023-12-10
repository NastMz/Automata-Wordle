from backend.app import socketio
from flask_socketio import emit
from ..core.automata import Automata

automata = Automata()


@socketio.on('start', namespace='/game')
def handle_start_game(msg):
    """
    Doc here
    """
    result = automata.update('start')
    emit('start', result)


@socketio.on('escribir', namespace='/game')
def handle_write(msg):
    """
    Doc here
    """
    result = automata.update('escribir', msg['word'])
    emit('escribir', result)


@socketio.on('verificar', namespace='/game')
def handle_verify(msg):
    """
    Doc here
    """
    result = automata.update('verificar')
    emit('verificar', result)
