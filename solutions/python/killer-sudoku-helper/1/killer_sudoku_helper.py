import itertools

DEFAULT_NUMS = set(range(1, 10))


def combinations(target: int, size: int, exclude: list[int] = []) -> list[list[int]]:
    """Find all valid digit combinations for a Killer Sudoku cage.

    Returns all possible combinations of digits that:
    - Sum to the target value
    - Use exactly 'size' digits
    - Don't contain any excluded digits
    - Use only digits 1-9 (standard Sudoku digits)
    - Don't repeat any digits within the combination

    Args:
        target: The sum that the cage must add up to
        size: The number of cells/digits in the cage
        exclude: List of digits that cannot be used (already present in
                the same row, column, or 3x3 box according to Sudoku rules).
                If None, no digits are excluded.

    Returns:
        A sorted list of lists, where each inner list contains the digits
        of one valid combination.

    Examples:
        >>> combinations(7, 3, [])
        [[1, 2, 4]]

        >>> combinations(10, 2, [])
        [[1, 9], [2, 8], [3, 7], [4, 6]]

        >>> combinations(10, 2, [1, 4])
        [[2, 8], [3, 7]]
    """
    return sorted(
        [
            sorted(list(combo))
            # Generate all possible combinations of the allowed digits of the given size
            for combo in itertools.combinations(
                # Allowed digits (1-9, excluding any in 'exclude')
                DEFAULT_NUMS - set(exclude),
                size,
            )
            # Filter combinations whose sum matches the target
            if sum(combo) == target
        ]
    )
