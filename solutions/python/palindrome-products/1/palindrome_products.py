from collections.abc import Callable


def largest(max_factor: int, min_factor: int = 0) -> tuple[int | None, list[list[int]]]:
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    return _get_with_pairs(min_factor, max_factor, _get_max)


def smallest(
    max_factor: int, min_factor: int = 0
) -> tuple[int | None, list[list[int]]]:
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    return _get_with_pairs(min_factor, max_factor, _get_min)


def _get_with_pairs(
    min_factor: int, max_factor: int, get: Callable[[int, int], int | None]
) -> tuple[int | None, list[list[int]]]:
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    num = get(min_factor, max_factor)
    if num is not None:
        return num, _get_pairs(num, min_factor, max_factor)
    return None, []


def _get_max(min_factor: int, max_factor: int) -> int | None:
    """Find largest palindrome by iterating through factor pairs in optimal order."""
    max_palindrome = 0

    # Iterate through factors in descending order for largest products first
    for factor in range(max_factor, min_factor - 1, -1):
        # Iterate through products down to factor^2
        for prod in range(factor * max_factor, factor * factor - 1, -factor):
            # Early termination: if product <= current max, break inner loop
            if prod <= max_palindrome:
                break

            if _is_palindrome(prod):
                max_palindrome = prod
                break  # Found palindrome for this factor, move to next factor

    return max_palindrome if max_palindrome else None


def _get_min(min_factor: int, max_factor: int) -> int | None:
    """Find smallest palindrome by iterating through factor pairs in optimal order."""
    inf = max_factor**2 + 1
    min_palindrome = inf

    # Iterate through factors in ascending order to find smallest palindrome first
    for factor in range(min_factor, max_factor + 1):
        # Iterate through products up to factor * max_factor
        for prod in range(factor**2, factor * max_factor + 1, factor):
            # Early termination: if product >= current min, break inner loop
            if prod >= min_palindrome:
                break

            if _is_palindrome(prod):
                min_palindrome = prod
                break  # Found palindrome for this factor, move to next factor

    return min_palindrome if min_palindrome < inf else None


def _is_palindrome(num: int) -> bool:
    """Check if a number is a palindrome without string conversion for better performance."""
    # Handle negative numbers, single digits, and numbers ending in 0
    if num < 0:
        return False
    if num < 10:
        return True
    if num % 10 == 0:
        return False

    rev = 0
    while num > rev:
        rev = rev * 10 + num % 10
        num //= 10

    return num == rev or num == rev // 10


def _get_pairs(prod: int, min_factor: int, max_factor: int) -> list[list[int]]:
    """Find all factor pairs of prod within the given range."""
    pairs: list[list[int]] = []

    # Check factors from max(min_factor, prod // max_factor) up to sqrt(prod) (or max_factor), to avoid duplicates and ensure both factors are within range
    for factor in range(
        max(min_factor, prod // max_factor), min(int(prod**0.5), max_factor) + 1
    ):
        if prod % factor == 0:
            pairs.append([factor, prod // factor])

    return pairs
