def square_of_sum(number: int) -> int:
    # Calculate the square of the sum of the first N natural numbers using the formula:
    # (1 + 2 + ... + N) = N * (N + 1) // 2 (Gauss's formula for the sum of an arithmetic series),
    # then square the result.
    return (number * (number + 1) // 2) ** 2


def sum_of_squares(number: int) -> int:
    # Calculate the sum of the squares of the first N natural numbers using the formula:
    # 1^2 + 2^2 + ... + N^2 = N * (N + 1) * (2N + 1) // 6 (Faulhaber's formula for the sum of squares)
    return number * (number + 1) * (2 * number + 1) // 6


def difference_of_squares(number: int) -> int:
    """
    Calculate the difference between the square of the sum and the sum of the squares
    of the first N natural numbers.

    For a given number N:
    - The square of the sum is (1 + 2 + ... + N)².
    - The sum of the squares is 1² + 2² + ... + N².

    Returns the result of (square of the sum) - (sum of the squares).

    Args:
        number (int): The upper bound of the range of natural numbers (inclusive).

    Returns:
        int: The difference between the square of the sum and the sum of the squares.
    """
    return square_of_sum(number) - sum_of_squares(number)
