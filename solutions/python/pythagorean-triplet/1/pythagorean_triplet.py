def triplets_with_sum(n: int) -> list[list[int]]:
    """
    Find all Pythagorean triplets [a, b, c] such that:
        a < b < c,
        a^2 + b^2 = c^2,
        a + b + c = n.

    Args:
        n (int): The sum of the triplet (a + b + c).

    Returns:
        list[list[int]]: A list of all Pythagorean triplets [a, b, c] where a + b + c = n.
    """
    res: list[list[int]] = []

    # Since a < b < c and a + b + c = n, the maximum value for a is less than n // 3
    for a in range(1, n // 3):
        # Derivation:
        # Given a^2 + b^2 = c^2 and a + b + c = n
        # Substitute c = n - a - b:
        #   a^2 + b^2 = (n - a - b)^2
        # Solve for b:
        #   b = (n(n - 2a)) // (2(n - a))
        numerator = n * (n - 2 * a)
        denominator = 2 * (n - a)

        # Ensure a < b < c, exit early
        if numerator <= a * denominator:
            break

        # b must be an integer, so numerator must be divisible by denominator
        if numerator % denominator != 0:
            continue

        b = numerator // denominator

        # c is determined by the sum
        c = n - a - b
        res.append([a, b, c])

    return res
