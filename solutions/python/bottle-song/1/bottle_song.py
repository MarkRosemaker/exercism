NUM_WORDS = [
    "no",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
]

FALL_LINE = "And if one green bottle should accidentally fall,"
WALL_SUFFIX = " hanging on the wall"


def recite(start: int, take: int = 1) -> list[str]:
    """Recite the lyrics to the "Ten Green Bottles" children's song.

    Generates verses of the repetitive song starting from a given number
    of bottles and continuing for a specified number of verses.

    Each verse follows the pattern:
    - "{Number} green bottle(s) hanging on the wall," (repeated twice)
    - "And if one green bottle should accidentally fall,"
    - "There'll be {number-1} green bottle(s) hanging on the wall."

    Args:
        start: The number of bottles to start with (1-10).
        take: The number of verses to generate (default: 1).

    Returns:
        A list of strings representing the song lyrics, with empty strings
        separating verses (except before the first verse).

    Example:
        >>> recite(3, 2)
        ['Three green bottles hanging on the wall,',
         'Three green bottles hanging on the wall,',
         'And if one green bottle should accidentally fall,',
         "There'll be two green bottles hanging on the wall.",
         '',
         'Two green bottles hanging on the wall,',
         'Two green bottles hanging on the wall,',
         'And if one green bottle should accidentally fall,',
         "There'll be one green bottle hanging on the wall."]
    """
    lines: list[str] = []
    for num_bottles in range(start, start - take, -1):
        if num_bottles != start:
            lines.append("")

        first = f"{bottle_words(num_bottles).capitalize()}{WALL_SUFFIX},"
        last = f"There'll be {bottle_words(num_bottles - 1)}{WALL_SUFFIX}."
        lines += [first, first, FALL_LINE, last]

    return lines


def bottle_words(num_bottles: int) -> str:
    return f"{NUM_WORDS[num_bottles]} green bottle{'s' if num_bottles != 1 else ''}"
