COLOR_TO_CODE = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

VALID_COLORS_STR = ", ".join(COLOR_TO_CODE)


def value(colors: list[str]) -> int:
    """
    Given a list of resistor color names, return the two-digit resistance value represented by the first two colors.

    Each color corresponds to a digit according to the resistor color code:
    black: 0, brown: 1, red: 2, orange: 3, yellow: 4, green: 5, blue: 6, violet: 7, grey: 8, white: 9.

    Only the first two colors in the input list are considered; any additional colors are ignored.

    Args:
        colors (list[str]): A list of color names representing the color bands on a resistor.

    Returns:
        int: The two-digit resistance value formed by the first two colors.

    Raises:
        ValueError: If fewer than two colors are provided, or if any of the first two colors is not a valid resistor color.

    Example:
        value(['brown', 'green']) -> 15
        value(['brown', 'green', 'violet']) -> 15
    """
    if len(colors) < 2:
        raise ValueError(
            "At least two colors are required to determine the resistor value."
        )

    res = 0
    for color in colors[:2]:
        color = color.lower()
        if color not in COLOR_TO_CODE:
            raise ValueError(
                f"'{color}' is not a valid resistor color. Valid colors are: {VALID_COLORS_STR}."
            )

        res = res * 10 + COLOR_TO_CODE[color]

    return res
