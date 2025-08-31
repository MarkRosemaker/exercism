def slices(series: str, length: int) -> list[str]:
    """
    Return all contiguous substrings (slices) of a given length from a string of digits.

    Given a string of digits, this function returns a list of all possible contiguous substrings
    of the specified length, in the order they appear in the input string.

    Parameters:
        series (str): The string of digits from which to extract slices.
        length (int): The length of each slice to extract.

    Returns:
        list[str]: A list of contiguous substrings of the specified length.

    Raises:
        ValueError: If the slice length is zero ("slice length cannot be zero").
        ValueError: If the slice length is negative ("slice length cannot be negative").
        ValueError: If the input series is empty ("series cannot be empty").
        ValueError: If the slice length is greater than the length of the series
                    ("slice length cannot be greater than series length").

    Examples:
        >>> slices("49142", 3)
        ['491', '914', '142']
        >>> slices("49142", 4)
        ['4914', '9142']
    """
    # Raise an error if the input series is empty.
    if not series:
        raise ValueError("series cannot be empty")
    # Raise an error if the slice length is not positive.
    if length <= 0:
        raise ValueError(
            f"slice length cannot be {'zero' if length == 0 else 'negative'}"
        )
    # Raise an error if the slice length exceeds the series length.
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")

    # Generate all contiguous substrings (slices) of the specified length.
    return [series[i : i + length] for i in range(len(series) - length + 1)]
