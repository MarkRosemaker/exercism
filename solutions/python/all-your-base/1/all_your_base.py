MIN_BASE = 2


def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Convert a number from one base to another.

    Args:
        input_base: The base of the input digits (must be >= 2)
        digits: List of digits in the input base
        output_base: The target base for conversion (must be >= 2)

    Returns:
        List of digits representing the same number in the output base

    Raises:
        ValueError: If bases are < 2 or digits are invalid for input base
    """
    if input_base < MIN_BASE:
        raise ValueError("input base must be >= 2")
    if output_base < MIN_BASE:
        raise ValueError("output base must be >= 2")

    num = 0
    for d in digits:
        if not (0 <= d < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")
        num = num * input_base + d

    if num == 0:
        return [0]

    result: list[int] = []
    while num:
        num, rem = divmod(num, output_base)
        result.append(rem)

    # Digits are collected in reverse order (least significant first), so reverse before returning.
    return result[::-1]
