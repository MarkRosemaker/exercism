# Each digit is represented by a tile of this size
DIGIT_HEIGHT = 4
DIGIT_WIDTH = 3

NUMBERS: dict[
    tuple[
        str,
        str,
        str,
        str,
    ],
    str,
] = {
    (" _ ", "| |", "|_|", "   "): "0",
    ("   ", "  |", "  |", "   "): "1",
    (" _ ", " _|", "|_ ", "   "): "2",
    (" _ ", " _|", " _|", "   "): "3",
    ("   ", "|_|", "  |", "   "): "4",
    (" _ ", "|_ ", " _|", "   "): "5",
    (" _ ", "|_ ", "|_|", "   "): "6",
    (" _ ", "  |", "  |", "   "): "7",
    (" _ ", "|_|", "|_|", "   "): "8",
    (" _ ", "|_|", " _|", "   "): "9",
}


def convert(input_grid: list[str]) -> str:
    """
    Convert a grid of pipes, underscores, and spaces representing OCR numbers into a string of digits.

    The input can be any size, as long as the number of rows is a multiple of 4 and the number of columns is a multiple of 3.
    Each digit is represented by a 3x4 tile (3 columns wide, 4 rows high) within the grid.

    Args:
        input_grid (list[str]): List of strings, each representing a row of the OCR input.

    Returns:
        str: The recognized number(s) as a string. Garbled numbers are replaced with '?'.
            Multiple numbers on separate lines are joined with commas.

    Raises:
        ValueError: If the number of input lines is not a multiple of four, or
            if the number of input columns is not a multiple of three, or if row lengths are inconsistent.

    Example:
        >>> convert([
        ...     '    _  _     _  _  _  _  _  _  ',
        ...     '  | _| _||_||_ |_   ||_||_|| | ',
        ...     '  ||_  _|  | _||_|  ||_| _||_| ',
        ...     '                              '])
        '1234567890'
    """
    num_lines = len(input_grid)
    if num_lines % DIGIT_HEIGHT != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    if not input_grid:
        return ""

    num_columns = len(input_grid[0])
    if num_columns % DIGIT_WIDTH != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    if any(len(row) != num_columns for row in input_grid):
        raise ValueError("Not all rows have the same number of columns")

    return ",".join(
        _parse_row(input_grid, row, num_columns)
        for row in range(0, num_lines, DIGIT_HEIGHT)
    )


def _parse_row(grid: list[str], row: int, num_columns: int) -> str:
    """
    Parse a single row (group of DIGIT_HEIGHT lines) into a string of digits.
    """
    return "".join(
        _parse_digit(grid, row, col) for col in range(0, num_columns, DIGIT_WIDTH)
    )


def _parse_digit(grid: list[str], row: int, col: int) -> str:
    """
    Parse a single digit tile at (row, col) in the grid.
    """
    return NUMBERS.get(
        # Extract the digit's OCR representation as a tuple of strings for lookup
        tuple[str, str, str, str](
            grid[r][col : col + DIGIT_WIDTH] for r in range(row, row + DIGIT_HEIGHT)
        ),
        "?",
    )
