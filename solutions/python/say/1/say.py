from typing import Generator

# Names for digits 1-9 (index 0 is empty for convenience)
DIGITS = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

# Special names for numbers 10-19
TEENS = {
    0: "ten",
    1: "eleven",
    2: "twelve",
    3: "thirteen",
    4: "fourteen",
    5: "fifteen",
    6: "sixteen",
    7: "seventeen",
    8: "eighteen",
    9: "nineteen",
}

# Names for multiples of ten from 20 to 90 (indices 2-9)
TENS = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

# Unit names for thousands, millions, billions, trillions (index 0 is empty)
UNITS = ["", "thousand", "million", "billion", "trillion"]


def chunk_to_words(idx: int, chunk: int) -> Generator[str]:
    """
    Convert a number from 0 to 999 into English words.
    Yields words in reverse order (unit, tens/ones, hundred).
    """
    # Extract ones, tens, and hundreds digits
    ones_digit = chunk % 10
    chunk //= 10

    tens_digit = chunk % 10
    chunk //= 10

    hundreds_digit = chunk % 10

    # Skip empty chunks (all digits zero)
    if ones_digit + tens_digit + hundreds_digit == 0:
        return

    # Yield unit name (thousand, million, etc.) if applicable
    if idx > 0:
        yield UNITS[idx]

    # Handle tens and ones places
    match tens_digit:
        case 0:
            # Only ones place
            if ones_digit > 0:
                yield DIGITS[ones_digit]
        case 1:
            yield TEENS[ones_digit]
        case _:
            # For 20-99
            if ones_digit > 0:
                yield f"{TENS[tens_digit]}-{DIGITS[ones_digit]}"
            else:
                yield TENS[tens_digit]

    # Handle hundreds place
    if hundreds_digit > 0:
        yield "hundred"
        yield DIGITS[hundreds_digit]


def chunk_generator(n: int):
    """
    Yield groups of three digits from the right (least significant chunk first).
    """
    while n > 0:
        yield n % 1000
        n //= 1000


def say(number: int) -> str:
    """
    Convert a non-negative integer (0 to 999,999,999,999) into its English words representation.

    Given an integer number, returns a string expressing the number in full English words,
    as it would be read aloud (e.g., 123 → "one hundred twenty-three").

    Parameters:
        number (int): The number to convert. Must be between 0 and 999,999,999,999 inclusive.

    Returns:
        str: The English words representation of the number.

    Raises:
        ValueError: If the input number is negative or greater than 999,999,999,999,
                    with the message "input out of range".
    """
    # Validate input range
    if number < 0 or 999_999_999_999 < number:
        raise ValueError("input out of range")

    # Special case for zero
    if number == 0:
        return "zero"

    # Process each chunk, collect words, and reverse to correct order
    return " ".join(
        reversed(
            [
                word
                for idx, chunk in enumerate(chunk_generator(number))
                for word in chunk_to_words(idx, chunk)
            ]
        )
    )
