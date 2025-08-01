def reverse(text: str) -> str:
    """
    Returns the reverse of the input string.

    Args:
        text (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    # In-place swap method
    chars = list(text)
    half_length = len(chars) // 2
    for i in range(half_length):
        j = len(chars) - i - 1
        chars[i], chars[j] = chars[j], chars[i]

    return "".join(chars)

    # Alternative methods:
    # Using list.reverse()
    # chars = list(text)
    # chars.reverse()
    # return "".join(chars)

    # Using reversed() function
    # return "".join(reversed(text))

    # Using slicing
    # return text[::-1]
