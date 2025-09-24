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
    if limit < 2:
        return []

    # Initialize a boolean list to track numbers up to the limit
    is_prime = [True] * (limit + 1)
    # 0 and 1 are not primes
    is_prime[0:2] = [False, False]

    # Mark multiples of each prime as non-prime
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            # Mark all multiples of p as non-prime
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False

    # Collect all numbers marked as prime
    return [i for i, prime in enumerate(is_prime) if prime]
