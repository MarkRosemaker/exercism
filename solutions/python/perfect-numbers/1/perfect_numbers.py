def classify(number: int) -> str:
    """
    A perfect number equals the sum of its positive divisors.

    Args:
        number (int): A positive integer.

    Returns:
        str: The classification of the input integer.
            Possible values are:
            - "perfect": if the number equals the sum of its proper divisors
            - "abundant": if the sum of its proper divisors is greater than the number
            - "deficient": if the sum of its proper divisors is less than the number

    Raises:
        ValueError: If the number is less than 1.
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum = _get_aliquot_sum(number)
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"


def _get_aliquot_sum(n: int) -> int:
    """
    Calculate the aliquot sum of a given integer.

    The aliquot sum of a number is the sum of its proper divisors (divisors excluding the number itself).
    For example, the aliquot sum of 12 is 1 + 2 + 3 + 4 + 6 = 16.

    Args:
        n (int): The integer for which to calculate the aliquot sum.

    Returns:
        int: The sum of the proper divisors of n.
    """
    # Special case: 1 has no proper divisors, so its aliquot sum is 0
    if n == 1:
        return 0

    # Start with 1, since 1 is a proper divisor of every number > 1
    sum_divisors = 1

    # Loop through possible divisors from 2 up to sqrt(n)
    stop = int(n**0.5) + 1
    for factor in range(2, stop):
        if n % factor == 0:
            # If factor divides n, add it to the sum
            sum_divisors += factor

            # If the paired divisor is different, add it as well
            other = n // factor
            if factor != other:
                sum_divisors += other

    # Return the sum of all proper divisors (aliquot sum)
    return sum_divisors
