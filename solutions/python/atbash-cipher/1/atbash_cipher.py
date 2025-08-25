# ATBASH_SUM is used to map a letter to its reversed counterpart in the alphabet.
# For a given lowercase letter c, chr(ATBASH_SUM - ord(c)) gives the Atbash cipher letter.
# This works because:
#   - ord('a') maps to ord('z'), ord('b') to ord('y'), ..., ord('z') to ord('a').
#   - ATBASH_SUM = ord('a') + ord('z')
#   - So, chr(ord('a') + ord('z') - ord(c)) = reversed letter.
ATBASH_SUM = ord("a") + ord("z")
GROUP_SIZE = 5


def encode(plain_text: str) -> str:
    """
    Encodes the given plain text using the Atbash cipher.

    The Atbash cipher is a simple substitution cipher that replaces each letter in the input
    with its counterpart from the reversed alphabet (e.g., 'a' <-> 'z', 'b' <-> 'y', etc.).
    Digits are left unchanged, and all other characters (such as punctuation and spaces) are excluded.
    The encoded output is grouped into fixed-length groups (traditionally 5 characters per group),
    separated by spaces.

    All output letters are in lowercase.

    Args:
        plain_text (str): The text to encode.

    Returns:
        str: The encoded text, grouped in fixed-length blocks and separated by spaces.

    Examples:
        encode("test") -> "gvhg"
        encode("x123 yes") -> "c123b vh"
    """
    res: list[str] = []
    for c in plain_text.lower():
        if c.isalpha():
            # Substitute letter with its Atbash cipher equivalent
            c = chr(ATBASH_SUM - ord(c))
        elif not c.isdigit():
            # Ignore non-alphabetic, non-digit characters
            continue

        # Insert a space after every GROUP_SIZE characters in the output.
        # This works by checking if the number of characters added so far is a multiple of GROUP_SIZE.
        # Since spaces are also added to res, we use (GROUP_SIZE + 1) in the modulus to account for the space itself.
        if len(res) % (GROUP_SIZE + 1) == GROUP_SIZE:
            res.append(" ")

        # Add the encoded character (letter or digit) to the result
        res.append(c)

    return "".join(res)


def decode(ciphered_text: str) -> str:
    """
    Decodes the given text encoded with the Atbash cipher.

    The Atbash cipher reverses each letter in the alphabet (e.g., 'a' <-> 'z', 'b' <-> 'y', etc.).
    Digits are left unchanged, and all other characters (such as spaces and punctuation) are ignored.

    Args:
        ciphered_text (str): The encoded text to decode.

    Returns:
        str: The decoded plain text.

    Examples:
        decode("vcvix rhn") -> "exercism"
        decode("gvhgr mt123 gvhgr mt") -> "testing123testing"
    """
    res: list[str] = []
    for c in ciphered_text.lower():
        if c.isalpha():
            # Decode the letter using Atbash cipher (reverse mapping)
            res.append(chr(ATBASH_SUM - ord(c)))
        elif c.isdigit():
            # Keep digits unchanged
            res.append(c)
        # Ignore non-alphabetic, non-digit characters (e.g., spaces, punctuation)

    return "".join(res)
