def distance(strand_a: str, strand_b: str) -> int:
    """
    Calculate the Hamming distance between two DNA strands.

    The Hamming distance is defined as the number of differing characters between two sequences of equal length.
    This function compares two DNA strands (strings containing the letters 'C', 'A', 'G', and 'T') and returns
    the count of positions at which the corresponding nucleotides are different.
    Note: Only the length of the strands is validated; this function does not check whether the characters are valid DNA nucleotides ('C', 'A', 'G', 'T').

    Parameters:
        strand_a (str): The first DNA strand.
        strand_b (str): The second DNA strand.

    Returns:
        int: The Hamming distance between the two strands.

    Raises:
        ValueError: If the input strands are not of equal length.

    Example:
        >>> distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
        7
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    return sum(a != b for a, b in zip(strand_a, strand_b))
