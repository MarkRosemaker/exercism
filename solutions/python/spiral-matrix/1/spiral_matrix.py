def spiral_matrix(size: int) -> list[list[int]]:
    """Generate a square matrix filled in clockwise spiral order.

    Creates a matrix where numbers 1 to size² follow a clockwise spiral path
    from outer edge to center: right → down → left → up.

    Args:
        size: Matrix dimension (0 returns empty list)

    Returns:
        Square matrix with numbers arranged in clockwise spiral

    Examples:
        >>> spiral_matrix(3)
        [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    """
    # Generate matrix by calculating the spiral value for each position
    return [[_get_num(size, row, col) for col in range(size)] for row in range(size)]


def _get_num(size: int, row: int, col: int) -> int:
    """Calculate the spiral number at position (row, col).

    Uses concentric ring math to determine the value without simulation.

    Args:
        size: Matrix dimension
        row: Row index
        col: Column index

    Returns:
        The spiral number at this position
    """
    # Determine which concentric ring this position belongs to
    # Ring 0 = outer perimeter, Ring 1 = next inner ring, etc.
    layer = min(row, col, size - 1 - row, size - 1 - col)

    # Calculate dimensions for this ring
    edge_length = size - 2 * layer - 1  # Length of one edge (excluding corners)
    far_edge = size - layer - 1  # Position of the opposite boundary

    # Calculate how many numbers come before this ring (base number for ring)
    base = 4 * layer * (size - layer) + 1

    # Determine position along the ring's clockwise path
    if row == layer:
        # Top edge: moving right (→)
        return base + col - layer
    if col == far_edge:
        # Right edge: moving down (↓)
        return base + edge_length + (row - layer)
    if row == far_edge:
        # Bottom edge: moving left (←)
        return base + 2 * edge_length + (far_edge - col)

    # Left edge: moving up (↑)
    return base + 3 * edge_length + (far_edge - row)
