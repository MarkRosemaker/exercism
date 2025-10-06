import math


def cipher_text(plain_text: str) -> str:
    """Encode text using the square cipher method.

    Given an English text, output the encoded version using the classic square code method.

    The encoding process:
    1. Normalize input: remove spaces and punctuation, convert to lowercase
    2. Arrange normalized text in a rectangle as square as possible
    3. Read down columns from left to right to create the cipher
    4. Output as space-separated chunks

    The rectangle dimensions (r rows × c columns) are determined by:
    - r * c >= length of normalized message
    - c >= r
    - c - r <= 1

    Args:
        plain_text: The input text to encode

    Returns:
        The encoded cipher text with chunks separated by spaces

    Example:
        >>> cipher_text("If man was meant to stay on the ground, god would have given us roots.")
        'imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau '
    """
    # Normalization: remove spaces and punctuation, convert to lowercase
    normalized = "".join(filter(str.isalnum, plain_text.lower()))
    if not normalized:
        return ""

    # Calculate the dimensions
    cols = math.ceil(math.sqrt(len(normalized)))
    rows = math.ceil(len(normalized) / cols)

    # Build the cipher matrix by filling columns left to right.
    matrix: list[list[str]] = [[] for _ in range(cols)]
    for i, char in enumerate(normalized):
        matrix[i % cols].append(char)

    # Pad the last columns with spaces if needed
    num_cells = cols * rows
    for i in range(len(normalized), num_cells):
        matrix[i % cols].append(" ")

    # Output space-separated column strings, matching the cipher specification
    return " ".join("".join(row) for row in matrix)
