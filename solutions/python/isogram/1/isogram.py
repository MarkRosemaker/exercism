def is_isogram(string: str) -> bool:
    """
    Determine if a string is an isogram.

    An isogram is a word or phrase without a repeating letter, ignoring spaces and hyphens.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string is an isogram, False otherwise.
    """
    # Clean solution: filter only alphabetic characters, convert to lowercase,
    # and check if the number of unique letters equals the total number of letters.
    letters = [c for c in string.lower() if c.isalpha()]  # or: "a" <= letter <= "z"
    return len(set(letters)) == len(letters)

    # Alternative: Exit early if a repeating letter is found (more efficient for long strings)
    # seen = set[str]()
    # for letter in string.lower():
    #     if "a" <= letter <= "z":
    #         if letter in seen:
    #             return False
    #         seen.add(letter)
    #
    # return True
