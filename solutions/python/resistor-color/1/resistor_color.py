COLORS_TO_CODE = {
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

COLORS = list(COLORS_TO_CODE.keys())


def color_code(color: str) -> int:
    """
    Return the numerical value associated with a given resistor color band.

    Args:
        color (str): The color name of the resistor band (e.g., 'red', 'green').

    Returns:
        int: The numerical value corresponding to the given color, where
             black=0, brown=1, red=2, orange=3, yellow=4, green=5,
             blue=6, violet=7, grey=8, white=9.

    Raises:
        ValueError: If the provided color is not a valid resistor color.

    This function helps to look up the numeric value for a resistor color band
    according to the standard electronic color code.
    """
    # Normalize the input
    color = color.lower()
    if color not in COLORS_TO_CODE:
        raise ValueError(
            f"'{color}' is not a valid resistor color. Valid colors are: {', '.join(COLORS)}."
        )

    return COLORS_TO_CODE[color]


def colors() -> list[str]:
    """
    Return the list of valid resistor color names.

    Returns:
        list[str]: A list of color names as strings.
    """
    return COLORS
