def factors(value: int) -> list[int]:
    """
    Compute the prime factors of a given natural number.

    A prime factor is a prime number that divides the given number exactly, without leaving a remainder.
    This function returns a list of prime factors in ascending order, including repeated factors for their multiplicity.

    Parameters:
        value (int): The natural number to factorize (must be greater than 1).

    Returns:
        list[int]: A list of prime factors of the input number.

    Example:
        >>> factors(60)
        [2, 2, 3, 5]
    """
    factors: list[int] = []  # List to store the prime factors

    n = 2  # Start checking for factors from the smallest prime number
    while n * n <= value:
        # While n divides value evenly, it's a prime factor
        while value % n == 0:
            factors.append(n)  # Add n to the list of factors
            value //= n  # Divide value by n and continue
        n += 1  # Move to the next possible factor

    if value > 1:
        # If value is greater than 1, it is a prime factor itself
        factors.append(value)

    return factors
