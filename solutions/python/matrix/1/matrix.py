class Matrix:
    """
    Represents a matrix of numbers parsed from a string with embedded newlines.

    Given a string like:
        '9 8 7\n5 3 2\n6 6 7'
    this class provides access to the rows and columns as lists of integers.

    The parsing strategy switches based on the length of the input string.
    If the string is shorter than PARSE_THRESHOLD characters, a simple split-based approach is used.
    For longer strings, a manual parsing strategy is used to avoid performance issues with very large inputs.

    Example:
        >>> m = Matrix('1 2 3\n4 5 6\n7 8 9')
        >>> m.row(2)
        [4, 5, 6]
        >>> m.column(3)
        [3, 6, 9]
    """

    # Stores the parsed matrix as a list of rows
    matrix: list[list[int]]

    # Threshold for switching parsing strategies; can be adjusted as needed.
    PARSE_THRESHOLD = 10000

    def __init__(self, matrix_string: str) -> None:
        """
        Initialize the Matrix from a string representation.

        Args:
            matrix_string (str): A string representing the matrix, with rows separated by newlines
                and numbers separated by spaces.
        """
        # For small strings, use split-based parsing (fast and readable)
        if len(matrix_string) < self.PARSE_THRESHOLD:
            self.matrix = [
                [int(n) for n in line.split()] for line in matrix_string.splitlines()
            ]
            return

        # For large strings, parse manually to avoid memory overhead
        self.matrix = []
        row: list[int] = []  # Current row being built
        num: str = ""  # Accumulates digits for the current number
        for c in matrix_string:
            if c.isdigit():
                num += c  # Build up the current number
                continue

            if num:
                # Add completed number to row
                row.append(int(num))
                num = ""
            if c == "\n":
                # Add completed row to matrix
                self.matrix.append(row)
                row = []  # Start a new row

        # Add the last number and row if present
        if num:
            row.append(int(num))
        if row:
            self.matrix.append(row)

    def row(self, index: int) -> list[int]:
        """
        Return the row at the given 1-based index.

        Args:
            index (int): The 1-based index of the row to retrieve.

        Returns:
            list[int]: The row as a list of integers.
        """
        # Return the (index-1)th row (1-based indexing)
        return self.matrix[index - 1]

    def column(self, index: int) -> list[int]:
        """
        Return the column at the given 1-based index.

        Args:
            index (int): The 1-based index of the column to retrieve.

        Returns:
            list[int]: The column as a list of integers.
        """
        # Return the (index-1)th element from each row (1-based indexing)
        return [row[index - 1] for row in self.matrix]
