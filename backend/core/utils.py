import os
import random
from backend.config.constants import FILE_PATH


def get_words():
    """
    Retrieve a list of words from the specified file.

    Reads a file containing a list of words and returns the list. The file path is determined by the constant FILE_PATH
    defined in the 'backend.config.constants' module.

    Returns:
        list: A list of words read from the file.

    Raises:
        FileNotFoundError: If the specified file is not found.
        ValueError: If the file is empty.
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
    Generate a random word from the list of words.

    Returns:
        str: A randomly chosen word from the list of words.
    """
    return random.choice(get_words())


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

    written_letters = list(word_write.lower())
    generated_letters = list(word_gen.lower())

    # Create a copy of the generated letters to mark the occurrences we have already used
    used_indices = set()

    for i, letter in enumerate(written_letters):
        if letter == generated_letters[i] and i not in used_indices:
            # The letter is in the correct position and has not been used before
            good_hints.append({"letter": letter, "position": i})
            used_indices.add(i)

    for i, letter_gen in enumerate(generated_letters):
        occurrences = [index for index, letter in enumerate(written_letters) if letter == letter_gen]

        for value in occurrences:
            if i != value and value not in used_indices:
                # The letter is in the generated word but not in the correct position
                # and has not been used before
                near_hints.append({"letter": written_letters[value], "position": value})
                used_indices.add(value)
                break

    for i, letter in enumerate(written_letters):
        if i not in used_indices:
            # The letter is in the generated word but in the incorrect position
            # or is not in the generated word
            bad_hints.append({"letter": letter, "position": i})

    hint = {"good": good_hints,
            "near": near_hints,
            "bad": bad_hints}
    return hint
