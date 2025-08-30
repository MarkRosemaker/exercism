import re

word_separator_pattern = re.compile(r"[\s\-]+")


def abbreviate(words: str) -> str:
    """
    Convert a phrase to its acronym.

    This function generates an acronym by taking the first letter of each word in the input phrase and converting it to uppercase. Hyphens are treated as word separators (like whitespace), while all other punctuation is removed from the input.

    Examples:
        abbreviate("As Soon As Possible") -> "ASAP"
        abbreviate("Liquid-crystal display") -> "LCD"
        abbreviate("Thank George It's Friday!") -> "TGIF"

    Args:
        words (str): The phrase to be converted into an acronym.

    Returns:
        str: The resulting acronym in uppercase letters.
    """
    return "".join(
        # Get first letter of each word, uppercase
        next((c.upper() for c in word if c.isalpha()), "")
        # Split phrase into words
        for word in word_separator_pattern.split(words)
    )
