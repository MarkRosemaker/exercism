from typing import Generator


class Luhn:
    """
    Implements the Luhn algorithm to validate numerical identifiers such as credit card numbers,
    bank account numbers, transaction codes, and tracking IDs.

    The Luhn algorithm works as follows:
    - Remove all spaces from the input string.
    - If the resulting string has length 1 or less, or contains any non-digit characters, it is invalid.
    - Starting from the second-to-last digit and moving left, double every second digit.
      If doubling results in a number greater than 9, subtract 9 from it.
    - Sum all the digits.
    - If the total sum is evenly divisible by 10, the number is valid.

    Args:
        card_num (str): The number to be validated, provided as a string. Spaces are allowed and ignored.

    Methods:
        valid() -> bool:
            Returns True if the number is valid according to the Luhn formula, False otherwise.

    Examples:
        >>> Luhn("4539 3195 0343 6467").valid()
        True
        >>> Luhn("066 123 478").valid()
        False
    """

    def __init__(self, card_num: str):
        # Remove spaces for consistent processing
        self.card_num = card_num.replace(" ", "")

    def valid(self) -> bool:
        return (
            # Validate input: must be all digits and at least two digits
            len(self.card_num) > 1
            and self.card_num.isdigit()
            and sum(
                # Apply Luhn doubling logic
                _luhn_doubling(
                    # Get digits from right to left
                    _digits_right_to_left(
                        # Convert card number to integer for digit extraction
                        int(self.card_num)
                    )
                )
            )
            % 10  # Valid if checksum is divisible by 10
            == 0
        )


def _digits_right_to_left(num: int) -> Generator[int, None, None]:
    """
    Yield digits of num from right to left (ones to highest place).
    Example: 123 -> yields 3, 2, 1
    """
    while num > 0:
        yield num % 10
        num //= 10


def _luhn_doubling(digits: Generator[int, None, None]) -> Generator[int, None, None]:
    """
    Apply Luhn doubling logic to a sequence of digits.
    Every second digit (from the right) is doubled; if result > 9, subtract 9.
    """
    should_double: bool = False
    for digit in digits:
        if should_double:
            # Double digit, subtract 9 if result > 9
            yield digit * 2 - 9 if digit > 4 else digit * 2
        else:
            yield digit
        should_double = not should_double
