def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """
    Transform legacy letter score data from a one-to-many mapping to a one-to-one mapping.

    Given a dictionary where each key is a point value and each value is a list of uppercase letters
    that share that point value, return a new dictionary mapping each lowercase letter to its point value.

    Args:
        legacy_data (dict[int, list[str]]): A dictionary mapping point values to lists of uppercase letters.

    Returns:
        dict[str, int]: A dictionary mapping each lowercase letter to its corresponding point value.

    Example:
        >>> transform({1: ["A", "E"], 2: ["D", "G"]})
        {"a": 1, "e": 1, "d": 2, "g": 2}
    """
    return {
        letter.lower(): score
        for score, letters in legacy_data.items()
        for letter in letters
    }
