def is_valid(isbn: str) -> bool:
    """
    Check if the provided ISBN-10 string is valid.

    Args:
        isbn (str): The ISBN-10 string to validate.

    Returns:
        bool: True if the ISBN is valid, False otherwise.
    """
    digits: list[int] = []
    for i, n in enumerate(isbn):
        if n == "-":
            if (
                i == 0  # dash at start
                or i == len(isbn) - 1  # dash at end
                or isbn[i - 1] == "-"  # consecutive dash
            ):
                return False  # Invalid: dash at start/end or consecutive dashes
            continue
        elif n.isdigit():
            digits.append(int(n))
        elif n == "X":
            if i != len(isbn) - 1:
                return False  # 'X' only allowed as the check digit (last character)
            digits.append(10)
        else:
            return False  # Invalid character

    return (
        # Ensure the ISBN has exactly 10 digits before validating the checksum
        len(digits) == 10
        # Checksum validation
        and sum((10 - i) * num for i, num in enumerate(digits)) % 11 == 0
    )
