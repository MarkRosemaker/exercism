from typing import Generator

AREA_CODE_LENGTH: int = 3  # NANP area code length
EXCHANGE_CODE_LENGTH: int = 3  # NANP exchange code length
ALLOWED_PUNCTUATION: set[str] = {
    "+",
    " ",
    ".",
    "-",
    "(",
    ")",
}  # Allowed formatting characters


class PhoneNumber:
    """
    Represents and validates a North American phone number (NANP).

    This class normalizes input phone numbers by removing formatting characters and country code,
    validates the number according to NANP rules, and provides formatted output.

    - Accepts numbers with various separators and optional country code (1).
    - Raises ValueError with descriptive messages for invalid numbers.
    - Provides a pretty() method for human-readable formatting.
    """

    def __init__(self, number: str) -> None:
        """
        Initialize and validate a phone number according to NANP rules.

        Args:
            number (str): The input phone number in any format (may include country code, separators, etc).

        Raises:
            ValueError: If the phone number is invalid for any NANP rule violation.
        """
        # Extract digits using a generator, validating as we go
        self.number: str = "".join(digit_gen(number))

        # Remove country code if present (NANP allows optional leading '1')
        if len(self.number) == 11:
            if self.number[0] != "1":
                raise ValueError("11 digits must start with 1")
            self.number = self.number[1:]

        # Split into area code, exchange code, and subscriber number
        self.area_code: str = self.number[:AREA_CODE_LENGTH]
        self.exchange_code: str = self.number[
            AREA_CODE_LENGTH : AREA_CODE_LENGTH + EXCHANGE_CODE_LENGTH
        ]
        self.subscriber_number: str = self.number[
            AREA_CODE_LENGTH + EXCHANGE_CODE_LENGTH :
        ]

        # Validate area and exchange code (cannot start with 0 or 1)
        for code, name in [
            (self.area_code, "area code"),
            (self.exchange_code, "exchange code"),
        ]:
            if code[0] == "0":
                raise ValueError(f"{name} cannot start with zero")
            if code[0] == "1":
                raise ValueError(f"{name} cannot start with one")

    def pretty(self) -> str:
        """
        Return the phone number in a human-readable format: (XXX)-XXX-XXXX

        Returns:
            str: The formatted phone number.
        """
        # Format the number for display
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"


def digit_gen(number: str) -> Generator[str, None, None]:
    """
    Generator that yields digits from the input string, ignoring allowed punctuation.

    Validates each character:
    - Yields digits
    - Skips allowed punctuation
    - Raises ValueError for letters or forbidden punctuation
    - Enforces digit count (10-11 digits allowed)

    Args:
        number (str): The input phone number string.

    Yields:
        str: Each digit character from the input.

    Raises:
        ValueError: If letters or forbidden punctuation are found, or digit count is invalid.
    """
    count: int = 0
    for c in number:
        if c.isdigit():
            count += 1
            if count > 11:
                # Early exit for overly long strings
                raise ValueError("must not be greater than 11 digits")
            yield c
        elif c in ALLOWED_PUNCTUATION:
            # Allowed formatting character, skip
            continue
        elif c.isalpha():
            # Letters are not permitted in phone numbers
            raise ValueError("letters not permitted")
        else:
            # Any other character is forbidden punctuation
            raise ValueError("punctuations not permitted")

    # Final check for minimum digit count
    if count < 10:
        raise ValueError("must not be fewer than 10 digits")
