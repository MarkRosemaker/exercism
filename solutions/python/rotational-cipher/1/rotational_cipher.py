ALPHABET_SIZE = ord("z") - ord("a") + 1


def rotate(text: str, key: int) -> str:
    """
    Rotates each alphabetic character in the input text by the specified key, preserving case.
    Non-alphabetic characters remain unchanged.

    Args:
        text (str): The input string to be rotated.
        key (int): The number of positions to shift each letter.

    Returns:
        str: The rotated string with each letter shifted by the key.
    """
    res = list(text)
    for i, c in enumerate(text):
        if not c.isalpha():
            # Skip non-alphabetic characters
            continue

        base = ord("A") if c.isupper() else ord("a")

        # Shift the character by 'key' positions within the alphabet, wrapping around if necessary
        res[i] = chr((ord(c) - base + key) % ALPHABET_SIZE + base)
    return "".join(res)
