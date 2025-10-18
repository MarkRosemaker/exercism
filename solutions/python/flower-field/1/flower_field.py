# Directions for checking all 8 adjacent squares (including diagonals)
# Starting from top-left and going clockwise: NW, N, NE, E, SE, S, SW, W
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def annotate(garden: list[str]) -> list[str]:
    """Add flower counts to empty squares in a Flower Field garden.

    This function takes a garden represented as a list of strings where each
    character is either a space (' ') for empty squares or an asterisk ('*')
    for flowers. It returns a new garden where each empty square is replaced
    with the count of adjacent flowers (1-8), or remains empty if no flowers
    are adjacent.

    Args:
        garden: A list of strings representing the garden board. Each string
               represents a row, with ' ' for empty squares and '*' for flowers.

    Returns:
        A list of strings representing the annotated garden with flower counts.

    Raises:
        ValueError: If the board is malformed (inconsistent row lengths or
                   invalid characters other than ' ' and '*').

    Example:
        >>> garden = [' * * ', '  *  ', '  *  ', '     ']
        >>> annotate(garden)
        ['1*3*1', '13*31', ' 2*2 ', ' 111 ']
    """
    # Handle empty garden case early
    if not garden:
        return []

    # Validate that all rows have consistent length
    num_cols = len(garden[0])
    if any(len(row) != num_cols for row in garden[1:]):
        raise ValueError("The board is invalid with current input.")

    # Validate that all characters are valid (space or asterisk only)
    if any(ch not in " *" for row in garden for ch in row):
        raise ValueError("The board is invalid with current input.")

    # Convert strings to mutable lists for easier manipulation
    grid: list[list[str]] = [list(row) for row in garden]

    # Process each cell in the garden to add flower counts
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            # Skip flowers - they don't need annotation
            if ch == "*":
                continue

            # Count adjacent flowers and update cell if any are found
            if count := sum(
                # Check if the adjacent position is within bounds
                0 <= r + dr < len(grid)
                and 0 <= c + dc < num_cols
                # Check if the adjacent cell contains a flower
                and grid[r + dr][c + dc] == "*"
                # Iterate through all 8 possible directions
                for dr, dc in DIRECTIONS
            ):
                # Replace empty space with flower count
                row[c] = str(count)

    return ["".join(row) for row in grid]
