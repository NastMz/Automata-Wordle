from .utils import generate_word, generate_hint


class Automata:
    """
    Class representing a simple automaton for managing the flow of a game.

    Attributes:
    - alphabet (set): The set of valid actions or transitions that the automaton can recognize.
    - states (set): The set of possible states that the automaton can be in during the game.
    - transitions (dict): A dictionary representing the possible transitions between states based on input actions.
    - initial_state (str): The initial state of the automaton when the game starts.
    - final_states (set): The set of states that, when reached, signify the end of the game.
    - current_state (str): The current state of the automaton during the game.

    Methods:
    - change_state(symbol: str) -> Union[bool, str]: 
        Changes the state of the automaton based on the given input transition.

        Args:
        - symbol (str): The transition to be applied.

        Returns:
        - bool or str: 
            - False if the transition is not valid.
            - True if a final state is reached, indicating the end of the game.
            - The new state if the transition is valid and a final state is not reached.
    """

    def __init__(self):
        """
        Initializes the automaton with the alphabet, states, transitions, and initial/final states.
        """
        # Define the alphabet
        self.alphabet = {'start', 'escribir', 'verificar', 'incorrecto',
                         'correcto', 'quedan_vidas', 'no_quedan_vidas'}

        # Define the states
        self.states = {'INICIAR_JUEGO', 'CARGAR_PALABRA', 'LEER_PALABRA',
                       'VERIFICAR_PALABRA', 'RESTAR_VIDA', 'DAR_PISTA', 'WIN', 'GAME_OVER'}

        # Define transitions
        self.transitions = {
            'INICIAR_JUEGO': {'start': {'CARGAR_PALABRA'}},
            'CARGAR_PALABRA': {'escribir': {'LEER_PALABRA'}},
            'LEER_PALABRA': {'escribir': {'LEER_PALABRA'}, 'verificar': {'VERIFICAR_PALABRA'}},
            'VERIFICAR_PALABRA': {'correcto': {'WIN'}, 'incorrecto': {'RESTAR_VIDA'}},
            'RESTAR_VIDA': {'quedan_vidas': {'DAR_PISTA'}, 'no_quedan_vidas': {'GAME_OVER'}},
            'DAR_PISTA': {'': {'LEER_PALABRA'}}
        }

        # Define initial, final and current states
        self.initial_state = 'INICIAR_JUEGO'
        self.final_states = {'WIN'}
        self.current_state = self.initial_state

        # Define var game
        self.life = 6
        self.word_gen = None
        self.word_write = None

    def change_state(self, symbol):
        """
        Changes the state of the automaton based on the given transition.

        Args:
        - symbol (str): The transition to be applied.

        Returns:
        - bool or str: False if the transition is not valid, True if a final state is reached, or the new state if the transition is valid and a final state is not reached.
        """
        # Handling final states
        if self.current_state == 'WIN':
            print(
                f'El juego ha terminado en el estado {self.current_state}. No se pueden realizar más transiciones.')
            return True

        # Get the next state
        next_state = next(iter(self.transitions.get(
            self.current_state, {}).get(symbol, set())), None)

        # Update the current state if the transition is valid
        if next_state:
            self.current_state = next_state
            return self.current_state
        else:
            print(f'Transición no válida ({symbol}) para el estado ({self.current_state})')
            return False

    def restart(self):
        """
        Doc here
        """
        self.current_state = self.initial_state
        self.life = 6

    def update(self, symbol, msg=None):
        """
        Doc here
        """
        if symbol == 'start':
            self.restart()
            if self.change_state(symbol) is False:
                return {'result': f'transición no válida ({symbol}) para el estado ({self.current_state})'}
            self.word_gen = generate_word()
            return {'result': {
                'word': self.word_gen
            }}

        if symbol == 'escribir':
            if self.change_state(symbol) is False:
                return {'result': f'transición no válida ({symbol}) para el estado ({self.current_state})'}
            self.word_write = msg
            if self.current_state == 'WIN':
                return (f'el juego ha terminado en el estado {self.current_state}. No se pueden realizar más '
                        f'transiciones.')
            else:
                return {'result': 'palabra leida'}

        if symbol == 'verificar':
            if self.change_state(symbol) is False:
                return {'result': f'transición no válida ({symbol}) para el estado ({self.current_state})'}
            if self.word_write == self.word_gen:
                self.change_state('correcto')
                return {'result': 'WIN'}
            else:
                self.change_state('incorrecto')
                self.life -= 1

            if self.life > 0:
                self.change_state('quedan_vidas')
                hint = generate_hint(self.word_write, self.word_gen)
                self.change_state('')
                if self.current_state == 'WIN':
                    return (f'el juego ha terminado en el estado {self.current_state}. No se pueden realizar más '
                            f'transiciones.')
                else:
                    return hint
            else:
                self.change_state('no_quedan_vidas')
                return {'result': 'GAME_OVER',
                        'answer': self.word_gen}
