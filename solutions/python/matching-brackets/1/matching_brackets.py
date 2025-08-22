def is_paired(input_string: str) -> bool:
    """
    Checks whether all brackets, braces, and parentheses in the input string are balanced and properly nested.

    Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, this function verifies that every opening bracket, brace, or parenthesis has a corresponding and correctly nested closing counterpart. All other characters in the string are ignored.

    Args:
        input_string (str): The string to be checked for balanced brackets, braces, and parentheses.

    Returns:
        bool: True if all brackets, braces, and parentheses are balanced and properly nested; False otherwise.

    Examples:
        >>> is_paired("{[()]}")
        True
        >>> is_paired("{what is (42)}?")
        True
        >>> is_paired("[text}")
        False
    """
    stack: list[str] = []
    for letter in input_string:
        match letter:
            case "{" | "[" | "(":
                stack.append(letter)
            case "]" | "}" | ")":
                # Convert closing to opening by manipulating the byte
                # For ')', ']', '}': their ASCII codes are +1, +2, +2 from their opening counterparts
                if not stack or stack.pop() != chr(
                    ord(letter) - (1 if letter == ")" else 2)
                ):
                    return False
            case _:
                pass
    return len(stack) == 0
