import re


def translate(text: str) -> str:
    """Translate a space-separated phrase from English to Pig Latin.

    Parameters
    - text: str -- one or more words separated by spaces.

    Returns
    - str: the phrase where each word has been converted to Pig Latin following
        the four rules described in the module docstring.

    Examples
    >>> translate("apple")
    'appleay'
    >>> translate("pig")
    'igpay'
    >>> translate("quick brown fox")
    'ickquay ownbray oxfay'
    """
    # Split the text into words, translate each, and join back
    return " ".join(translate_word(word) for word in text.strip().split())


def translate_word(word: str) -> str:
    """Translate a single English word to Pig Latin following Rules 1-4.

    Rules (short):
    1. Vowel/"xr"/"yt" start -> append "ay".
    2. Leading consonant cluster -> move to end + "ay".
    3. Consonant* + "qu" -> move consonant*+"qu" to end + "ay".
    4. Consonant+ followed by "y" -> move preceding consonants to end + "ay".

    Parameters
    - word: str -- single word to translate (lowercase expected for current logic).

    Returns
    - str: translated word.

    Examples
    >>> translate_word("apple")
    'appleay'
    >>> translate_word("pig")
    'igpay'
    >>> translate_word("quick")
    'ickquay'
    >>> translate_word("rhythm")
    'ythmrhay'
    """
    # Rule 1: Words that start with a vowel sound, "xr", or "yt"
    if re.match(r"^(?:[aeiou]|xr|yt)", word, re.IGNORECASE):
        return f"{word}ay"

    # Rule 3: Words that start with consonant(s) followed by "qu"
    if match := re.match(r"^([^aeiou]*qu)(.*)", word, re.IGNORECASE):
        prefix, rest = match.groups()
        return f"{rest}{prefix}ay"

    # Rule 4: Words that start with consonant(s) followed by "y"
    if match := re.match(r"^([^aeiou]+)y(.*)", word, re.IGNORECASE):
        consonants, rest = match.groups()
        return f"y{rest}{consonants}ay"

    # Rule 2: Words that start with one or more consonants
    if match := re.match(r"^([^aeiou]+)(.*)", word, re.IGNORECASE):
        consonants, rest = match.groups()
        return f"{rest}{consonants}ay"

    # Fallback: Handles any word not matched by the above rules (should not occur)
    return f"{word}ay"
