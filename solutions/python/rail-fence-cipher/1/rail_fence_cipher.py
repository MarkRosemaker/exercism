from typing import Generator


def encode(message: str, rails: int) -> str:
    """
    Encode a message using the rail fence cipher.

    Arranges the message in a zigzag pattern across the specified number of rails,
    then reads the characters row by row to create the encoded message.

    Args:
        message: The plaintext message to encode
        rails: The number of rails (rows) to use in the zigzag pattern

    Returns:
        The encoded message as a string
    """
    if rails == 1:
        return message

    n = len(message)

    # Read characters in rail order: rail 0, then rail 1, etc.
    return "".join(
        [
            message[pos]
            for rail in range(rails)
            for pos in _positions_for_rail(rails, n, rail)
        ]
    )


def decode(encoded_message: str, rails: int) -> str:
    """
    Decode a rail fence cipher message.

    Takes an encoded message and reconstructs the original by placing characters
    back into their zigzag positions, then reading in the original order.

    Args:
        encoded_message: The encoded message to decode
        rails: The number of rails used in the original encoding

    Returns:
        The decoded (original) message as a string
    """
    if rails == 1:
        return encoded_message

    n = len(encoded_message)
    result = [""] * n

    # Place encoded characters back into their original zigzag positions
    encoded_pos = 0
    for rail in range(rails):
        for original_pos in _positions_for_rail(rails, n, rail):
            result[original_pos] = encoded_message[encoded_pos]
            encoded_pos += 1

    return "".join(result)


def _positions_for_rail(rails: int, n: int, rail: int) -> Generator[int, None, None]:
    """
    Generate the positions where characters appear on a specific rail in the zigzag pattern.

    For rails 0 and (rails-1), characters appear at regular intervals.
    For middle rails, characters alternate between two different step sizes as the
    zigzag pattern moves up and down.

    Args:
        rails: Total number of rails in the cipher
        n: Length of the message
        rail: The specific rail number (0-indexed)

    Yields:
        Position indices where characters appear on this rail
    """
    if rail == 0 or rail == rails - 1:
        # Top and bottom rails: characters appear at regular intervals
        cycle = 2 * (rails - 1)  # Full cycle length (down + up)
        yield from range(rail, n, cycle)
        return

    # Middle rails: zigzag creates two different step sizes
    step_down = 2 * (rails - rail - 1)  # Steps when moving down
    step_up = 2 * rail  # Steps when moving up

    i = rail  # Start at the rail's first position
    down = True  # Track zigzag direction
    while i < n:
        yield i
        # Alternate between down and up steps
        i += step_down if down else step_up
        down = not down
