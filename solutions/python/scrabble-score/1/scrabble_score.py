LETTER_VALUES = {
    **dict.fromkeys("AEIOULNRST", 1),
    **dict.fromkeys("DG", 2),
    **dict.fromkeys("BCMP", 3),
    **dict.fromkeys("FHVWY", 4),
    **dict.fromkeys("K", 5),
    **dict.fromkeys("JX", 8),
    **dict.fromkeys("QZ", 10),
}


def score(word: str) -> int:
    """
    Calculate the Scrabble score for a given word.

    Each letter in the word is assigned a point value according to Scrabble rules:
    - A, E, I, O, U, L, N, R, S, T: 1 point
    - D, G: 2 points
    - B, C, M, P: 3 points
    - F, H, V, W, Y: 4 points
    - K: 5 points
    - J, X: 8 points
    - Q, Z: 10 points

    The function sums the values of all letters in the input word, ignoring case.

    Non-letter characters are ignored and do not contribute to the score.

    Args:
        word (str): The word to score.

    Returns:
        int: The total Scrabble score for the word.

    Example:
        >>> score("quirky")
        22
    """
    return sum(LETTER_VALUES.get(c, 0) for c in word.upper())
