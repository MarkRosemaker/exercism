ACTIONS = ["wink", "double blink", "close your eyes", "jump"]


def commands(binary_str: str) -> list[str]:
    """
    Converts a binary string representing a secret handshake code into a list of handshake actions.

    The handshake is determined by the rightmost five digits of the binary string, with each digit representing an action:
    - 1st digit (rightmost): "wink"
    - 2nd digit: "double blink"
    - 3rd digit: "close your eyes"
    - 4th digit: "jump"
    - 5th digit: If set, reverses the order of the actions.

    Only the rightmost five bits of the input are used, which is enforced by masking with `0b11111`.

    Parameters:
        binary_str (str): A binary string of up to 5 digits representing the handshake code.

    Returns:
        list[str]: A list of handshake actions in the correct order.
    """
    # Validate input: must be a non-empty binary string containing only '0' and '1'
    if not binary_str or any(c not in "01" for c in binary_str):
        raise ValueError(
            "Input must be a non-empty binary string containing only '0' and '1'."
        )

    # Convert binary string to integer
    code = int(binary_str, 2)

    res: list[str] = []
    for i, action in enumerate(ACTIONS):
        if code & (1 << i):
            res.append(action)

    if code & (1 << 4):
        res.reverse()

    return res
