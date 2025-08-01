import string

ALPHABET_SET = set(string.ascii_lowercase)


def is_pangram(sentence: str) -> bool:
    """
    Checks if the given sentence is a pangram.

    Args:
        sentence (str): The sentence to check.

    Returns:
        bool: True if the sentence is a pangram, False otherwise.
    """
    # Convert the sentence to lowercase to ensure case-insensitive comparison
    sentence = sentence.lower()

    # Method 1: Check if all lowercase letters are present in the sentence
    return ALPHABET_SET.issubset(set(sentence))

    # Alternative Method: Check using set comprehension
    # return len({letter for letter in sentence if "a" <= letter <= "z"}) == 26
