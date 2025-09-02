import re

# Pattern explanation: (\d*) matches zero or more digits (the count), (\D) matches a single non-digit character (the letter/space)
RLE_DECODE_PATTERN = re.compile(r"(\d*)(\D)")


def decode(string: str) -> str:
    """
    Decodes a run-length encoded string into its original uncompressed form.

    Run-length encoding (RLE) compresses data by replacing sequences of the same character
    with a single character and a count. This function reverses that process, reconstructing
    the original string from its encoded form.

    Each number in the encoded string represents how many times the following character
    should appear in the output. If a character is not preceded by a number, it appears once.

    Parameters:
        string (str): The run-length encoded string to decode. The string contains only
                      uppercase/lowercase letters and whitespace, with numbers representing
                      counts for the following character.

    Returns:
        str: The decoded, original uncompressed string.

    Example:
        decode("2AB3CD4E") -> "AABCCCDEEEE"
        decode("12WB12W3B24WB") -> "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    """
    res: list[str] = []  # List to accumulate decoded characters

    # Use the compiled regex to find all (optional digits)(single non-digit) pairs
    for match in RLE_DECODE_PATTERN.finditer(string):
        # If a number is present, use it as count; otherwise, default to 1
        count = int(match.group(1)) if match.group(1) else 1
        # Repeat the character 'count' times and add to result
        res.append(match.group(2) * count)

    # Join all parts into the final decoded string
    return "".join(res)


def encode(string: str) -> str:
    """
    Encodes a string using run-length encoding (RLE).

    Consecutive runs of the same character are replaced by the count followed by the character.
    Single characters are not preceded by a count.

    Args:
        string (str): The input string to encode. Contains only A-Z, a-z, and whitespace.

    Returns:
        str: The run-length encoded string.

    Examples:
        >>> encode("AABCCCDEEEE")
        '2AB3CD4E'
        >>> encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB")
        '12WB12W3B24WB'
        >>> encode("")
        ''
    """
    if not string:
        return ""

    res: list[str] = []  # List to accumulate encoded parts
    count = 1  # Counter for consecutive characters
    prev = string[0]  # Previous character

    # Iterate over the string starting from the second character (the first character is handled by initialization)
    for c in string[1:]:
        if c == prev:
            count += 1  # Increment count if same as previous
        else:
            # Encode the repeating characters
            if count > 1:
                res.append(str(count))
            res.append(prev)

            # Reset count and character
            count = 1
            prev = c

    # Handle the last run after the loop
    if count > 1:
        res.append(str(count))
    res.append(prev)

    # Join all parts into the final encoded string
    return "".join(res)
