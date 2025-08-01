MAPPING = {"G": "C", "C": "G", "T": "A", "A": "U"}


def to_rna(dna_strand: str) -> str:
    """
    Transcribes a DNA strand into its corresponding RNA complement.

    Given a DNA sequence, returns the RNA sequence by replacing each nucleotide with its RNA complement:
        - 'G' is replaced with 'C'
        - 'C' is replaced with 'G'
        - 'T' is replaced with 'A'
        - 'A' is replaced with 'U'

    Parameters:
        dna_strand (str): A string representing the DNA sequence, consisting of the characters 'A', 'C', 'G', and 'T'.

    Returns:
        str: The transcribed RNA sequence as a string.
    """

    return "".join(MAPPING[c] for c in dna_strand)
