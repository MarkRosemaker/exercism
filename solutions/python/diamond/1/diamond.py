BASE = ord("A")


def rows(letter: str) -> list[str]:
    """
    Generates the rows of a diamond shape for a given uppercase letter.

    The diamond starts with 'A' at the top and bottom, and has the supplied letter at its widest point.
    Each row is a string, padded with spaces to ensure the diamond is horizontally and vertically symmetric.
    The diamond has a square shape (width equals height), and the letters form a diamond pattern.
    The top half of the diamond lists letters in ascending order from 'A' to the given letter,
    while the bottom half mirrors the top half in descending order.

    Args:
        letter (str): An uppercase letter from 'A' to 'Z' indicating the widest point of the diamond.
            The input is assumed to be a single uppercase letter; invalid input is not handled.

    Returns:
        list[str]: A list of strings, each representing a row of the diamond.
    """
    diamond_size = ord(letter) - BASE + 1

    def build_row(i: int) -> str:
        # Calculate the number of spaces on each side
        outer_spaces = " " * (diamond_size - i - 1)

        # Get the current letter
        current_letter = chr(BASE + i)
        if i == 0:
            # First row, only one letter
            return outer_spaces + current_letter + outer_spaces

        # Rows with two letters and inner spaces
        inner_spaces = " " * (i * 2 - 1)
        return (
            outer_spaces + current_letter + inner_spaces + current_letter + outer_spaces
        )

    # Build the top half including the middle row
    res = [build_row(i) for i in range(diamond_size)]

    # Mirror the top half to create the bottom half, excluding the middle row
    res += res[-2::-1]

    return res
