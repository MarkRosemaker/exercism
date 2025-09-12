BOARD_SIZE = 8


class Queen:
    """
    Represents a queen on a chessboard. Validates position on an 8x8 board.

    Raises:
        ValueError: If row or column is negative or not on the board.
    """

    def __init__(self, row: int, column: int) -> None:
        """
        Initialize a Queen at the given row and column.

        Args:
            row (int): The row position (0-7).
            column (int): The column position (0-7).

        Raises:
            ValueError: If row or column is negative or not on the board.
        """
        # Validate row and column positions
        for pos, name in ((row, "row"), (column, "column")):
            if pos < 0:
                raise ValueError(f"{name} not positive")
            if pos >= BOARD_SIZE:
                raise ValueError(f"{name} not on board")

        # Store the queen's position
        self.row: int = row
        self.column: int = column

    def can_attack(self, another_queen: "Queen") -> bool:
        """
        Determine if this queen can attack another queen.

        Queens can attack if they share the same row, column, or diagonal.

        Args:
            another_queen (Queen): The other queen to check against.

        Returns:
            bool: True if the queens can attack each other, False otherwise.

        Raises:
            ValueError: If both queens are on the same square.
        """
        # Check if both queens are on the same square
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        # Check if queens are on the same row, column, or diagonal
        return (
            self.row == another_queen.row  # Same row
            or self.column == another_queen.column  # Same column
            or self.row - self.column
            == another_queen.row - another_queen.column  # Same diagonal (\)
            or self.row + self.column
            == another_queen.row + another_queen.column  # Same diagonal (/)
        )
