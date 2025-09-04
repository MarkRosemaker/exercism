CARDINALS: tuple[str, ...] = (
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
)

GIFTS: tuple[str, ...] = (
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
)


def recite(start_verse: int, end_verse: int) -> list[str]:
    """
    Return the lyrics of "The Twelve Days of Christmas" for the specified range of verses.

    Each verse of the song builds cumulatively on the previous verses, listing all the gifts given on each day.
    The function returns a list of strings, where each string is a verse of the song, starting from `start_verse` and ending with `end_verse` (inclusive).

    Args:
        start_verse (int): The verse number to start from (1-based).
        end_verse (int): The verse number to end with (1-based, inclusive).

    Returns:
        list[str]: A list of verses from the song, each as a string, in order from `start_verse` to `end_verse`.

    Example:
        recite(1, 3) returns the first three verses of the song as a list of strings.
    """
    return [recite_verse(verse) for verse in range(start_verse, end_verse + 1)]


def recite_verse(verse: int) -> str:
    """
    Generate the lyrics for a specific verse of the "Twelve Days of Christmas" song.

    Args:
        verse (int): The verse number (1-based) to generate the lyrics for.

    Returns:
        str: The complete lyrics for the specified verse.

    Note:
        This function relies on the global lists CARDINALS and GIFTS to construct the verse.
    """
    return f"On the {CARDINALS[verse - 1]} day of Christmas my true love gave to me: {', '.join(reversed(GIFTS[1:verse]))}{', and ' if verse > 1 else ''}{GIFTS[0]}."
