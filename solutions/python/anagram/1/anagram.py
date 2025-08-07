def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """
    Finds all anagrams of a given target word from a list of candidate words.

    An anagram is a word formed by rearranging the letters of another word, using all the original letters exactly once.
    The comparison is case-insensitive, and a word is not considered an anagram of itself.

    Parameters:
        word (str): The target word to find anagrams of.
        candidates (list[str]): A list of candidate words to check against the target word.

    Returns:
        list[str]: A list of candidate words that are anagrams of the target word.

    Examples:
        >>> find_anagrams("stone", ["stone", "tones", "banana", "tons", "notes", "Seton"])
        ['tones', 'notes', 'Seton']
    """
    word = word.lower()
    sorted_word = sorted(word)

    anagrams: list[str] = []
    for candidate in candidates:
        candidate_lower = candidate.lower()

        # Check that word is not itself
        if candidate_lower == word:
            continue

        # Save sort computation by checking length
        if len(candidate_lower) != len(word):
            continue

        if sorted_word == sorted(candidate_lower):
            anagrams.append(candidate)

    return anagrams
