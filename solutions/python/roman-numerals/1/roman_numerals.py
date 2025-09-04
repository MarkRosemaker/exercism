ROMAN_NUMERALS: tuple[tuple[str, int], ...] = (
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
)


def roman(number: int) -> str:
    """
    Convert an integer to its Roman numeral representation.

    Given an integer `number` in the range 1 to 3999 (inclusive), returns a string
    representing the number as a Roman numeral. Roman numerals use the following
    symbols and values:

        M = 1000, D = 500, C = 100, L = 50, X = 10, V = 5, I = 1

    The same letter cannot be used more than three times in succession. For numbers
    like 4, 9, 40, 90, 400, and 900, a subtraction notation is used (e.g., IV for 4,
    IX for 9, XL for 40, XC for 90, CD for 400, CM for 900).

    The returned Roman numeral string will use the largest possible values first,
    ordered from left to right.

    Args:
        number (int): The integer to convert (1 <= number <= 3999).

    Returns:
        str: The Roman numeral representation of the input number.

    Raises:
        ValueError: If `number` is not in the range 1 to 3999 (inclusive).
    """
    if number < 1 or number > 3999:
        raise ValueError("number must be in the range 1 to 3999")

    roman_numeral_parts: list[str] = []
    for symbol, value in ROMAN_NUMERALS:
        if count := number // value:
            roman_numeral_parts.append(symbol * count)
            number %= value

    return "".join(roman_numeral_parts)
