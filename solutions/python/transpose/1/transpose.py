def transpose(text: str) -> str:
    """
    Transpose the input text as if it were a matrix of characters.

    Each line in the input is treated as a row. The output will have columns become rows and rows become columns.
    If input rows have different lengths, pad to the left with spaces (not to the right) so that all characters are present in the transposed output.
    Spaces in the bottom-most rows of a column are preserved in the transposed output as right-most characters in the corresponding row.

    Examples:
        ABC\nDEF   ->   AD\nBE\nCF
        ABC\nDE    ->   AD\nBE\nC
        AB\nDEF   ->   AD\nBE\n F
    """
    # Return immediately for empty input
    if not text:
        return ""

    # Split input into lines
    lines: list[str] = text.splitlines()
    num_lines: int = len(lines)

    # Efficiently compute the maximum width for each row and all rows below it.
    # After reversal, row_max_widths[k] is the max length of any row from k to the last.
    row_max_widths: list[int] = [len(lines[-1])]
    for i in range(num_lines - 2, -1, -1):
        row_max_widths.append(max(row_max_widths[-1], len(lines[i])))
    row_max_widths.reverse()

    def get_row_limit(col: int) -> int:
        """
        Returns the first row index where col >= row_max_widths[row], or num_lines if not found.
        """
        return next(
            (row for row, width in enumerate(row_max_widths) if col >= width),
            num_lines,
        )

    # Build the transposed output:
    # For each column, include only rows where the column index is less than the max length for that row.
    # Pad with spaces if the row is too short for the column.
    # We use generator expressions to to save memory.
    return "\n".join(
        (
            "".join(
                (
                    lines[row][col] if col < len(lines[row]) else " "
                    for row in range(get_row_limit(col))
                )
            )
            for col in range(row_max_widths[0])
        )
    )
