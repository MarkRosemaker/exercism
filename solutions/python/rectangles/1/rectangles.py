CORNER = "+"
HORIZONTAL_EDGE = "-"
VERTICAL_EDGE = "|"
HORIZONTAL_CHARS = CORNER + HORIZONTAL_EDGE
VERTICAL_CHARS = CORNER + VERTICAL_EDGE


def rectangles(strings: list[str]) -> int:
    """Count the rectangles in an ASCII diagram.

    A rectangle is defined by:
    - Four corners marked with '+' characters
    - Horizontal edges made of '-' or '+' characters
    - Vertical edges made of '|' or '+' characters

    The function searches for all possible rectangles by finding top-left corners
    ('+' characters) and then checking for valid bottom-left, top-right, and
    bottom-right corners that form complete rectangles with proper edges.

    Args:
        strings: A list of strings representing the ASCII diagram. Each string
                represents a row, and all strings are assumed to have equal length.

    Returns:
        The number of rectangles found in the diagram.

    Example:
        >>> diagram = [
        ...     "   +--+",
        ...     "  ++  |",
        ...     "+-++--+",
        ...     "|  |  |",
        ...     "+--+--+"
        ... ]
        >>> rectangles(diagram)
        6
    """
    count = 0

    # Find rectangles by checking each '+' as a top-left corner
    for top, row in enumerate(strings):
        for left, ch in enumerate(row):
            if ch != CORNER:
                continue

            # Find bottom-left corners below this position
            bottom_rows: list[int] = []
            for y in range(top + 1, len(strings)):
                char_below = strings[y][left]
                if char_below == CORNER:
                    bottom_rows.append(y)
                elif char_below != VERTICAL_EDGE:
                    break

            # Find top-right corners to the right of this position
            for r in range(left + 1, len(strings[top])):
                char_right = strings[top][r]

                if char_right == HORIZONTAL_EDGE:
                    continue
                if char_right != CORNER:
                    break  # line interrupted

                # Check each bottom-left corner for complete rectangles
                for b in bottom_rows:
                    # Verify bottom-right corner exists
                    if strings[b][r] != CORNER:
                        continue

                    # Validate remaining edges
                    if all(
                        c in HORIZONTAL_CHARS for c in strings[b][left + 1 : r]
                    ) and all(
                        strings[y][r] in VERTICAL_CHARS for y in range(top + 1, b)
                    ):
                        count += 1
    return count
