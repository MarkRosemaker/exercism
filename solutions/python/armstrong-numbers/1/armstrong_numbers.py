def is_armstrong_number(number: int) -> bool:
    """
    Check if a number is an Armstrong number.

    Parameters:
        number (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    if number < 0:
        return False

    num_digits = len(str(number))
    return sum(int(digit) ** num_digits for digit in str(number)) == number
