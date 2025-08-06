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

TOLERANCE_COLOR_TO_PERCENT = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}

VALID_TOLERANCES = ", ".join(TOLERANCE_COLOR_TO_PERCENT)


def resistor_label(colors: list[str]) -> str:
    """
    Converts a list of resistor color bands into a human-readable resistance label.

    The function supports 1-band (black only), 4-band, and 5-band resistor color codes.
    For 4-band resistors, the bands represent: [value1, value2, multiplier, tolerance].
    For 5-band resistors, the bands represent: [value1, value2, value3, multiplier, tolerance].
    The function returns the resistance value in ohms, kiloohms, megaohms, or teraohms,
    along with the tolerance.

    Args:
        colors (list[str]): List of color names representing the resistor bands.

    Returns:
        str: The formatted resistor label, e.g., "33 kiloohms ±0.5%".

    Raises:
        ValueError: If an invalid color or tolerance is provided, or if the number of bands is not 1, 4, or 5.

    Examples:
        resistor_label(["orange", "orange", "black", "green"]) -> "33 ohms ±0.5%"
        resistor_label(["orange", "orange", "orange", "grey"]) -> "33 kiloohms ±0.05%"
        resistor_label(["orange", "orange", "blue", "red"]) -> "33 megaohms ±2%"
        resistor_label(["orange", "orange", "orange", "black", "green"]) -> "333 ohms ±0.5%"
    """
    # Normalize all color names to lowercase for case-insensitive matching
    colors = [color.lower() for color in colors]

    match len(colors):
        case 1:
            if colors[0] == "black":
                return "0 ohms"
            raise ValueError("At least four colors must be provided.")
        case 4 | 5:
            *values, multiplier, tolerance = colors
        case _:
            raise ValueError(
                "Only 4-band or 5-band resistor color codes are supported."
            )

    # Validate all color bands first
    for color in values + [multiplier]:
        if color not in COLOR_TO_CODE:
            raise ValueError(
                f"'{color}' is not a valid resistor color. Valid colors are: {VALID_COLORS_STR}."
            )

    # Calculate ohms value
    ohms: int = 0
    for color in values:
        ohms *= 10
        ohms += COLOR_TO_CODE[color]

    ohms *= 10 ** COLOR_TO_CODE[multiplier]

    if tolerance not in TOLERANCE_COLOR_TO_PERCENT:
        raise ValueError(
            f"'{tolerance}' is not a valid tolerance color. Valid tolerance colors are: {VALID_TOLERANCES}."
        )

    # Convert ohms to string with appropriate SI prefix
    ohms_str = f"{ohms} ohms"
    for value, prefix in SI_PREFIXES:
        if ohms < value:
            continue

        val = ohms / value
        formatted_val = int(val) if val.is_integer() else val
        ohms_str = f"{formatted_val} {prefix}ohms"
        break

    return f"{ohms_str} ±{TOLERANCE_COLOR_TO_PERCENT[tolerance]}"
