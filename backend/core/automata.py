from .utils import generate_word, generate_hint, get_words


class Automata:
    """
    Class representing a simple automaton for managing the flow of a game.

    Attributes:
        alphabet (set): The set of valid actions or transitions that the automaton can recognize.
        states (set): The set of possible states that the automaton can be in during the game.
        transitions (dict): A dictionary representing the possible transitions between states based on input actions.
        initial_state (str): The initial state of the automaton when the game starts.
        final_states (set): The set of states that, when reached, signify the end of the game.
        current_state (str): The current state of the automaton during the game.
        life (int): The number of lives or attempts available in the game.
        word_gen (str): The randomly generated word for the game.
        word_write (str): The word input by the player.

    Methods:
        __new__(cls, *args, **kwargs) -> Automata: Implements the Singleton pattern to allow only one instance of the class.
        __init__(self): Initializes the Automata class.
        change_state(symbol: str) -> Union[bool, str]: Changes the state of the automaton based on the given input transition.
        restart(): Resets the game to its initial state.
        update(symbol: str, msg=None) -> dict: Updates the game state based on the input symbol and an optional message.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Singleton pattern implementation. Only one instance of the class can exist at a time.

        Returns:
            Automata: The instance of the Automata class.
        """
        if not cls._instance:
            cls._instance = super(Automata, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Initializes the Automata class.

        The Automata class represents a simple game automaton designed for word-guessing games.
        It manages the flow of the game through different states and transitions based on player actions.

        Attributes:
            alphabet (set): The set of valid actions or transitions that the automaton can recognize.
            states (set): The set of possible states that the automaton can be in during the game.
            transitions (dict): A dictionary representing the possible transitions between states based on input actions.
            initial_state (str): The initial state of the automaton when the game starts.
            final_states (set): The set of states that, when reached, signify the end of the game.
            current_state (str): The current state of the automaton during the game.
            life (int): The number of lives or attempts available in the game.
            word_gen (str): The randomly generated word for the game.
            word_write (str): The word input by the player.
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
        Changes the state of the automaton based on the given input transition.

        Args:
            symbol (str): The transition to be applied.

        Returns:
            bool or str:
                - False if the transition is not valid.
                - True if a final state is reached, indicating the end of the game.
                - The new state if the transition is valid and a final state is not reached.
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
        Resets the game to its initial state, allowing the player to start a new game.

        The restart method resets the game by setting the current state back to the initial state
        and restoring the initial number of lives. This method is called when the player chooses to
        start a new game or after the current game has ended.

        Args:
            None

        Returns:
            None

        """
        self.current_state = self.initial_state
        self.life = 6

    def update(self, symbol, msg=None):
        """
        Updates the game state based on the input symbol and an optional message.

        Args:
            symbol (str): The action or transition to be applied.
            msg (str, optional): An optional message associated with the action.

        Returns:
            dict:
                Dictionary with the result of the game depending on the state and the symbol.
        """
        if symbol == 'start':
            self.restart()
            if self.change_state(symbol) is False:
                return {'result': f'transición no válida ({symbol}) para el estado ({self.current_state})'}
            self.word_gen = generate_word()

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
            # verificar si la palabra existe en el diccionario y no son letras aleatorias
            if self.word_write.lower() not in get_words():
                return {'result': 'INVALID_WORD'}

            if self.change_state(symbol) is False:
                return {'result': f'transición no válida ({symbol}) para el estado ({self.current_state})'}
            if self.word_write.lower() == self.word_gen.lower():
                self.change_state('correcto')
                return {'result': 'WIN'}
            else:
                self.change_state('incorrecto')
                self.life -= 1

            if self.life > 0:
                self.change_state('quedan_vidas')
                hint = generate_hint(self.word_write.lower(), self.word_gen.lower())
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
