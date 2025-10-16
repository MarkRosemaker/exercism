from typing import Generator

# Number of data bits per byte (excluding continuation bit)
NUM_BITS = 7

# Continuation bit mask (0x80 = 10000000 binary)
CONTINUATION_BIT = 1 << NUM_BITS

# Data bits mask (0x7F = 01111111 binary)
DATA_MASK = CONTINUATION_BIT - 1


def encode(numbers: list[int]) -> list[int]:
    """
    Encode a list of integers using Variable Length Quantity encoding.

    Each integer is encoded as a sequence of bytes where:
    - The first 7 bits of each byte contain data
    - The 8th bit (MSB) is set to 1 for all bytes except the last
    - The last byte has the MSB set to 0
    - Multi-byte numbers are encoded in big-endian order

    Args:
        numbers: List of non-negative integers to encode (32-bit max)

    Returns:
        List of encoded bytes as integers (0-255 range)

    Example:
        encode([0x00, 0x40, 0x7F, 0x80]) → [0x00, 0x40, 0x7F, 0x81, 0x00]
    """
    return [byte for num in numbers for byte in _encode(num)]


def _encode(n: int) -> Generator[int, None, None]:
    if n == 0:
        yield 0
        return

    # Calculate how many bytes we need by finding the highest set bit
    byte_count = (n.bit_length() - 1) // NUM_BITS + 1

    # Build bytes directly in big-endian order
    for i in range(byte_count - 1, 0, -1):
        # Extract 7 bits at position i and set continuation bit
        yield (n >> i * NUM_BITS) & DATA_MASK | CONTINUATION_BIT

    # Last byte, no continuation bit
    yield n & DATA_MASK


def decode(bytes_: list[int]) -> list[int]:
    """
    Decode a list of VLQ-encoded bytes back to integers.

    Reads the encoded bytes and reconstructs the original integers by:
    - Accumulating 7-bit data chunks in big-endian order
    - Using the MSB as a continuation flag
    - Completing a number when a byte with MSB=0 is encountered

    Args:
        bytes_: List of VLQ-encoded bytes (integers 0-255)

    Returns:
        List of decoded integers

    Raises:
        ValueError: If the sequence is incomplete (ends with continuation bit set)

    Example:
        decode([0x00, 0x40, 0x7F, 0x81, 0x00]) → [0x00, 0x40, 0x7F, 0x80]
    """
    # The last byte must not have the continuation bit set
    if bytes_[-1] & CONTINUATION_BIT:
        raise ValueError("incomplete sequence")

    res: list[int] = []
    n = 0
    for b in bytes_:
        # Shift previous data left by 7 bits and add new 7-bit chunk
        n = (n << NUM_BITS) | (b & DATA_MASK)

        # If continuation bit is clear, this is the last byte of the number
        if (b & CONTINUATION_BIT) == 0:
            res.append(n)
            n = 0  # Reset accumulator for next number

    return res
