import os
import random
from backend.config.constants import FILE_PATH


def generate_word():
    """
    Generates a random word from a file.

    This function reads a file containing a list of words, randomly selects one word,
    and returns it. The file path is determined by the 'FILE_PATH' constant defined in
    the 'backend.config.constants' module.

    Returns:
        str: A randomly chosen word from the file.

    Raises:
        ValueError: If the file is empty.
        FileNotFoundError: If the file specified by 'FILE_PATH' is not found.

    """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, FILE_PATH)

    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()
            if not words:
                raise ValueError(
                    "The file is empty. Please provide a file with words.")
            return random.choice(words)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")


def generate_hint(word_write, word_gen):
    """
    Generates hints based on the written word and the generated word.

    This function compares the written word with the generated word and generates hints
    indicating correct letters in the correct position ('good'), correct letters in the
    wrong position ('near'), and incorrect letters ('bad').

    Args:
        word_write (str): The word written by the player.
        word_gen (str): The randomly generated word.

    Returns:
        dict: A dictionary containing hints categorized as 'good', 'near', and 'bad'.
            Example:
            {
                "good": [{"word": "a", "position": 0}],
                "near": [{"word": "b", "position": 1}],
                "bad": [{"word": "c", "position": 2}]
            }
    """
    good_hints = []
    near_hints = []
    bad_hints = []

    written_letters = list(word_write)
    generated_letters = list(word_gen)

    # Creamos una copia de las letras generadas para marcar las ocurrencias que ya hemos utilizado
    used_indices = set()

    for i, letter in enumerate(written_letters):
        if letter == generated_letters[i] and i not in used_indices:
            # La letra está en la posición correcta y no ha sido utilizada antes
            good_hints.append({"word": letter, "position": i})
            used_indices.add(i)

    for i, letter_gen in enumerate(generated_letters):
        occurrences = [index for index, letter in enumerate(written_letters) if letter == letter_gen]

        for value in occurrences:
            if i != value and value not in used_indices:
                # La letra está en la palabra generada, pero no en la posición correcta
                # y no ha sido utilizada antes
                near_hints.append({"word": written_letters[value], "position": value})
                used_indices.add(value)
                break

    for i, letter in enumerate(written_letters):
        if i not in used_indices:
            # La letra está en la palabra generada, pero en una posición incorrecta
            # o no está en la palabra generada
            bad_hints.append({"word": letter, "position": i})

    hint = {"good": good_hints,
            "near": near_hints,
            "bad": bad_hints}
    return hint
