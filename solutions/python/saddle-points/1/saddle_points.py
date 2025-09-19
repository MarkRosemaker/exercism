def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    """
    Find saddle points in a matrix representing tree heights for tree house placement.

    A saddle point is a location that is:
    - The maximum value in its row (tallest tree east-west for best sunrise/sunset views)
    - The minimum value in its column (shortest tree north-south to minimize climbing)

    Args:
        matrix: A 2D list of integers representing tree heights. Rows represent
                east-west direction, columns represent north-south direction.
                Must be a regular matrix (all rows have the same length).

    Returns:
        A list of dictionaries, each containing the row and column (1-indexed)
        of a saddle point. Returns empty list if no saddle points exist.

    Raises:
        ValueError: If the matrix is irregular (rows have different lengths).

    Example:
        >>> matrix = [[9, 8, 7, 8], [5, 3, 2, 4], [6, 6, 7, 1]]
        >>> saddle_points(matrix)
        [{'row': 2, 'column': 1}]

    Note:
        Row and column indices in the returned dictionaries are 1-indexed,
        not 0-indexed like typical Python arrays.
    """
    res: list[dict[str, int]] = []

    # Handle empty matrix
    if not matrix:
        return res

    # Verify the matrix is regular
    num_columns: int = len(matrix[0])
    if not all(len(row) == num_columns for row in matrix):
        raise ValueError("irregular matrix")

    # Precompute column minimums
    column_minimums: list[int] = [
        min(row[c] for row in matrix) for c in range(num_columns)
    ]

    for row_index, row in enumerate(matrix):
        row_maximum: int = max(row)
        for col_index, value in enumerate(row):
            if value == row_maximum == column_minimums[col_index]:
                res.append({"row": row_index + 1, "column": col_index + 1})

    return res
