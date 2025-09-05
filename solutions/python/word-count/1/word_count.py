import re
from collections import Counter

# Regular expression to match words and numbers in a sentence.
# - [a-z]+('[a-z]+)? matches words with optional contractions (e.g., "don't", "you're").
#   - [a-z]+ matches the main word part.
#   - ('[a-z]+)? optionally matches an apostrophe followed by more letters (for contractions).
# - \d+ matches standalone numbers.
# The pattern is case-insensitive due to re.IGNORECASE.
WORD_PATTERN = re.compile(r"[a-z]+('[a-z]+)?|\d+", re.IGNORECASE)


def count_words(sentence: str) -> dict[str, int]:
    """
    Count the occurrences of each word in a given subtitle sentence.

    Words are defined as sequences of ASCII characters separated by any punctuation or whitespace,
    except for apostrophes within contractions (e.g., "don't" is a single word).
    Numbers are considered words. Words are case insensitive.

    Args:
        sentence (str): The subtitle sentence to analyze.

    Returns:
        dict[str, int]: A dictionary mapping each word (in lowercase) to its count in the sentence.
    """
    return Counter((match.group().lower() for match in WORD_PATTERN.finditer(sentence)))
