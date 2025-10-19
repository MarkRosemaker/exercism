def fence_pattern(rails: int, n: int):
    """
    Generate the rail fence pattern as (rail_number, position) pairs.

    This function creates the core mapping for the zigzag pattern by calculating
    which rail each position belongs to, then sorting by rail number.
    """
    # Full cycle length: down (rails-1) + up (rails-1)
    cycle = 2 * (rails - 1)

    # For each position pos, calculate which rail it belongs to
    return sorted(
        (
            # Calculate rail number using modular arithmetic
            (pos % cycle)
            if (pos % cycle) < rails  # Going down: rail = position % cycle
            else cycle - (pos % cycle),  # Going up: rail = cycle - (position % cycle)
            pos,  # Original position
        )
        for pos in range(n)
    )


def encode(msg: str, rails: int):
    """
    Encode message by reading characters in rail order.

    The fence_pattern gives us (rail, position) pairs sorted by rail.
    We extract the positions and read the message characters in that order.
    """
    # fence_pattern returns [(rail, pos), ...] sorted by rail
    # We want just the positions, ignoring the rail numbers
    return "".join(msg[pos] for _, pos in fence_pattern(rails, len(msg)))


def decode(msg: str, rails: int):
    """
    Decode message by placing characters back to their original positions.

    We pair each character from the encoded message with its fence pattern info,
    then sort by original position to reconstruct the message.
    """
    return "".join(
        ch
        for _, ch in sorted(
            # Pair each encoded character with its (rail, original_position) info
            zip(fence_pattern(rails, len(msg)), msg),
            # Sort by original position (the second element of the fence pattern tuple)
            # This puts characters back in their original order
            key=lambda pair: pair[0][1],
        )
    )
