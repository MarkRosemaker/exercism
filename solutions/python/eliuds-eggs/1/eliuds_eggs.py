def egg_count(display_value: int) -> int:
    """
    Returns the number of 1s in the binary representation of display_value.
    """
    count = 0
    while display_value > 0:
        count += display_value % 2
        display_value //= 2

    return count
