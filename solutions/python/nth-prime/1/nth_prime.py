primes: list[int] = [2, 3]


def prime(number: int) -> int:
    """
    Returns the nth prime number.

    Args:
        number (int): The position of the prime number to retrieve (1-based index).

    Returns:
        int: The nth prime number.

    Raises:
        ValueError: If number is less than 1, indicating malformed input.

    Example:
        prime(6)  # Returns 13, since the 6th prime is 13.
    """
    # Check for invalid input: zero or negative numbers
    if number == 0:
        raise ValueError("there is no zeroth prime")
    if number < 0:
        raise ValueError("number must not be negative")

    # Start searching for primes from the last known prime
    candidate = primes[-1]
    # Continue until we have found enough primes
    while len(primes) < number:
        candidate += 2  # Only check odd numbers (even numbers > 2 are not prime)
        sqrtNum = int(candidate**0.5)  # Calculate square root for optimization
        for factor in [p for p in primes if p <= sqrtNum]:
            if candidate % factor == 0:
                # If divisible by any known prime, candidate is not prime
                break
        else:
            # If no factors up to sqrt(candidate), candidate is prime
            primes.append(candidate)

    # Return the nth prime (1-based index)
    return primes[number - 1]
