"""
A solution for the Hex/Polygon/CON-TAC-TIX game.

This module implements a game solver for Hex, an abstract board game where two players
place stones on a parallelogram with hexagonal fields. The goal is to connect stones
from one side of the board to the opposite side.

Game Rules:
- Player O wins by connecting the top side to the bottom side
- Player X wins by connecting the left side to the right side
- The board uses hexagonal adjacency (6 neighbors per cell)
- Games can be asymmetric (different board dimensions or piece counts)
"""

from typing import Literal

Player = Literal["O", "X"]

# Hexagonal grid movement deltas for the 6 adjacent cells
# In a hexagonal grid, each cell has exactly 6 neighbors
DELTAS: list[tuple[int, int]] = [
    (-1, 0),  # up-left
    (-1, 1),  # up-right
    (0, 1),  # right
    (1, 0),  # down-right
    (1, -1),  # down-left
    (0, -1),  # left
]


class ConnectGame:
    """
    A game solver for the Hex/Polygon/CON-TAC-TIX board game.

    This class represents a Hex game board and provides functionality to determine
    the winner based on the current board state.

    Board Representation:
    - '.' represents an empty cell
    - 'O' represents Player O's stone
    - 'X' represents Player X's stone
    - Spaces in the input are ignored (removed during parsing)

    Victory Conditions:
    - Player O wins by creating a connected path from top to bottom
    - Player X wins by creating a connected path from left to right
    - Connection uses hexagonal adjacency (6 neighbors per cell)

    Example board:
        . O . X .
         . X X O .
          O O O X .
           . X O X O
            X O O O X
    """

    def __init__(self, board: str) -> None:
        """
        Initialize a new Hex game from a string representation.

        Args:
            board: String representation of the game board where each line
                  represents a row. Spaces are ignored and removed.

        Example:
            board = ". O . X .\n . X X O .\n  O O O X ."
        """
        self.matrix: list[str] = [line.replace(" ", "") for line in board.splitlines()]
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])

    def get_winner(self) -> str:
        """
        Determine the winner of the current game state.

        Uses flood-fill algorithm to check connectivity:
        1. For Player O: Start from top edge, check if bottom edge is reachable
        2. For Player X: Start from left edge, check if right edge is reachable

        Returns:
            'O' if Player O has won (connected top to bottom)
            'X' if Player X has won (connected left to right)
            '' if no winner yet
        """
        # Track which cells have been visited during flood-fill
        connected = [[False for _ in range(self.width)] for _ in range(self.height)]

        def flood_fill(row: int, col: int, player: str) -> None:
            """Mark all connected stones of the same player type."""
            if connected[row][col] or self.matrix[row][col] != player:
                return

            # Mark as visited
            connected[row][col] = True

            # Check all 6 hexagonal neighbors
            for dr, dc in DELTAS:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < self.height and 0 <= new_col < self.width:
                    flood_fill(new_row, new_col, player)

        # Check Player O victory: top to bottom connection
        # Start flood-fill from all O stones on the top edge
        for c in range(self.width):
            flood_fill(0, c, "O")

        # Check if any bottom edge cell is connected
        if any(connected[-1]):
            return "O"

        # Reset connected matrix for Player X check
        connected = [[False for _ in range(self.width)] for _ in range(self.height)]

        # Check Player X victory: left to right connection
        # Start flood-fill from all X stones on the left edge
        for r in range(self.height):
            flood_fill(r, 0, "X")

        # Check if any right edge cell is connected
        if any(connected[r][-1] for r in range(self.height)):
            return "X"

        # No winner found
        return ""
