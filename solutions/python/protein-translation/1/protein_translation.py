CODON_GROUPS: dict[tuple[str, ...], str] = {
    ("AUG",): "Methionine",
    ("UUU", "UUC"): "Phenylalanine",
    ("UUA", "UUG"): "Leucine",
    ("UCU", "UCC", "UCA", "UCG"): "Serine",
    ("UAU", "UAC"): "Tyrosine",
    ("UGU", "UGC"): "Cysteine",
    ("UGG",): "Tryptophan",
}

# Flatten the CODON_GROUPS mapping so each codon string maps directly to its protein name.
CODON_PROTEIN_MAP = {
    codon: protein for codons, protein in CODON_GROUPS.items() for codon in codons
}

STOP_CODONS = {"UAA", "UAG", "UGA"}

CODON_LENGTH = 3


def proteins(strand: str) -> list[str]:
    """
    Translates an RNA strand into a list of proteins (amino acids).

    Given an RNA sequence as a string, this function splits the sequence into codons (groups of three nucleotides)
    and translates each codon into its corresponding protein name according to the standard genetic code.
    Translation stops if a STOP codon is encountered; any codons after a STOP codon are ignored.

    Args:
        strand (str): The RNA sequence to be translated, consisting of characters 'A', 'U', 'G', and 'C'.

    Returns:
        list[str]: A list of protein names corresponding to the codons in the input strand, in order of translation.
                   Translation stops at the first STOP codon, if present.

    Raises:
        KeyError: If the strand contains a codon that is not recognized in the codon-to-protein mapping.

    Examples:
        >>> proteins("AUGUUUUCU")
        ['Methionine', 'Phenylalanine', 'Serine']

        >>> proteins("AUGUUUUCUUAAAUG")
        ['Methionine', 'Phenylalanine', 'Serine']
    """
    proteins: list[str] = []
    for i in range(0, len(strand) - CODON_LENGTH + 1, CODON_LENGTH):
        codon = strand[i : i + CODON_LENGTH]
        if codon in STOP_CODONS:
            return proteins

        proteins.append(CODON_PROTEIN_MAP[codon])
    return proteins
