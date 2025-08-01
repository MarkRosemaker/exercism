# Cache to store previously computed Collatz steps for optimization
__collatz_cache: dict[int, int] = {1: 0}  # 1 requires 0 steps


def steps(number: int) -> int:
    """
    Calculate the number of steps required to reach 1 using the Collatz Conjecture.

    Given a positive integer, repeatedly apply the following rules:
    - If the number is even, divide it by 2.
    - If the number is odd, multiply it by 3 and add 1.
    Count the number of steps taken to reach 1.

    Parameters:
        number (int): A positive integer to start the Collatz sequence.

    Returns:
        int: The number of steps required to reach 1.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    original_number = number
    steps: int = 0
    while number > 1:
        # Check if the result for this number is already cached
        if number in __collatz_cache:
            steps += __collatz_cache[number]
            break

        # Do the Collatz step
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        steps += 1

    # Cache the result for the original number
    __collatz_cache[original_number] = steps
    return steps
