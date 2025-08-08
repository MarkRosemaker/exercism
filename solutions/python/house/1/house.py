PHRASES: list[tuple[str, str]] = [
    ("horse and the hound and the horn", "belonged to"),
    ("farmer sowing his corn", "kept"),
    ("rooster that crowed in the morn", "woke"),
    ("priest all shaven and shorn", "married"),
    ("man all tattered and torn", "kissed"),
    ("maiden all forlorn", "milked"),
    ("cow with the crumpled horn", "tossed"),
    ("dog", "worried"),
    ("cat", "killed"),
    ("rat", "ate"),
    ("malt", "lay in"),
    ("house", "Jack built."),
]


def recite(start_verse: int, end_verse: int) -> list[str]:
    """
    Generate the cumulative rhyme 'This is the House That Jack Built.'

    The function will generate the requested verses in order, following the
    cumulative structure of the rhyme.

    Args:
        start_verse (int): The starting verse number (1-indexed, inclusive).
        end_verse (int): The ending verse number (1-indexed, inclusive).

    Returns:
        list[str]: A list of strings, each representing a verse from the rhyme,
                   starting from start_verse to end_verse (inclusive).
    """
    return [recite_verse(verse) for verse in range(start_verse, end_verse + 1)]


def recite_verse(verse: int) -> str:
    """
    Construct a single verse of the cumulative rhyme.

    Args:
        verse (int): The verse number (1-indexed).

    Returns:
        str: The verse as a string.
    """
    start = len(PHRASES) - verse
    return f"This is {' '.join(f'the {subject} that {verb}' for subject, verb in PHRASES[start:])}"
