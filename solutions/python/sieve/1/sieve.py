def primes(limit: int) -> list[int]:
    """
    Generate all prime numbers less than or equal to a given limit using the Sieve of Eratosthenes algorithm.

    Args:
        limit (int): The upper bound (inclusive) for generating prime numbers. Must be greater than or equal to 2.

    Returns:
        list[int]: A list of all prime numbers less than or equal to the given limit, in increasing order.

    Example:
        >>> primes(10)
        [2, 3, 5, 7]
    """
    # Initialize a set with all numbers from 2 up to the limit (inclusive)
    primes_set = set(range(2, limit + 1))

    # Iterate over each number from 2 up to the square root of the limit
    for prime in range(2, int(limit**0.5) + 1):
        # If the number is still in the set, it is a prime
        if prime in primes_set:
            # Remove multiples of the current prime
            primes_set -= set(range(prime * prime, limit + 1, prime))

    return sorted(primes_set)
