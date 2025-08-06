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

SI_PREFIXES: list[tuple[int, str]] = [
    (10**12, "tera"),
    (10**9, "giga"),
    (10**6, "mega"),
    (10**3, "kilo"),
]


def label(colors: list[str]) -> str:
    """
    Returns the resistance value of a resistor based on its color bands.

    Parameters:
        colors (list[str]): A list of at least three color names representing the resistor bands.

    Returns:
        str: The resistance value formatted with the appropriate SI prefix and 'ohms' unit.

    Raises:
        ValueError: If fewer than three colors are provided or if an invalid color is given.
    """
    if len(colors) < 3:
        raise ValueError("At least three colors must be provided.")

    first, second, third = (color.lower() for color in colors[:3])

    for color in (first, second, third):
        if color not in COLOR_TO_CODE:
            raise ValueError(
                f"'{color}' is not a valid resistor color. Valid colors are: {VALID_COLORS_STR}."
            )

    ohms: int = COLOR_TO_CODE[first] * 10 + COLOR_TO_CODE[second]
    ohms *= 10 ** COLOR_TO_CODE[third]

    for value, prefix in SI_PREFIXES:
        if ohms >= value and ohms % value == 0:
            return f"{ohms // value} {prefix}ohms"
    return f"{ohms} ohms"
