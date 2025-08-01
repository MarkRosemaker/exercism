def square(number: int) -> int:
    """
    Calculate the number of grains of wheat on a specific square of a chessboard.

    Each square on the chessboard contains double the grains of the previous square,
    starting with 1 grain on the first square. This function returns the number of grains
    on the given square.

    Args:
        number (int): The square number (1 through 64).

    Returns:
        int: The number of grains on the specified square.

    Raises:
        ValueError: If the square number is not between 1 and 64 (inclusive).
    """
    # Check if the square number is valid (between 1 and 64)
    if 0 < number <= 64:
        # The number of grains on a given square is 2^(number-1)
        return 2 ** (number - 1)

    # Raise an error if the square number is out of range
    raise ValueError("square must be between 1 and 64")


def total() -> int:
    """
    Calculate the total number of grains of wheat on a chessboard.

    Returns:
        int: The total number of grains, calculated as the sum of a geometric series
        where each square contains double the grains of the previous one, starting
        with 1 grain on the first square (2^0) up to 2^63 on the 64th square.
    """
    # The total number of grains on the chessboard is the sum of a geometric series:
    # 2^0 + 2^1 + ... + 2^63 = 2^64 - 1
    return 2**64 - 1
