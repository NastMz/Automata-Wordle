import os
import random
from backend.config.constants import FILE_PATH


def get_words():
    """
    Doc here
    """
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, FILE_PATH)

    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()
            if not words:
                raise ValueError(
                    "The file is empty. Please provide a file with words.")
            return words
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")


def generate_word():
    """
    Doc here
    """
    return random.choice(get_words())


def generate_hint(word_write, word_gen):
    """
    Generates a hint based on the written and generated words.

    Returns:
    - dict: A dictionary containing 'good' and 'near' hints.
    """
    good_hints = []
    near_hints = []
    bad_hints = []

    written_letters = list(word_write.lower())
    generated_letters = list(word_gen.lower())

    # Creamos una copia de las letras generadas para marcar las ocurrencias que ya hemos utilizado
    used_indices = set()

    for i, letter in enumerate(written_letters):
        if letter == generated_letters[i] and i not in used_indices:
            # La letra está en la posición correcta y no ha sido utilizada antes
            good_hints.append({"letter": letter, "position": i})
            used_indices.add(i)

    for i, letter_gen in enumerate(generated_letters):
        occurrences = [index for index, letter in enumerate(written_letters) if letter == letter_gen]

        for value in occurrences:
            if i != value and value not in used_indices:
                # La letra está en la palabra generada, pero no en la posición correcta
                # y no ha sido utilizada antes
                near_hints.append({"letter": written_letters[value], "position": value})
                used_indices.add(value)
                break

    for i, letter in enumerate(written_letters):
        if i not in used_indices:
            # La letra está en la palabra generada, pero en una posición incorrecta
            # o no está en la palabra generada
            bad_hints.append({"letter": letter, "position": i})

    hint = {"good": good_hints,
            "near": near_hints,
            "bad": bad_hints}
    return hint
