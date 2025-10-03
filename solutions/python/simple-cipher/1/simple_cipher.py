import secrets
import string

DEFAULT_KEY_LEN = 100

LOWERCASE_A_ORD = ord("a")
ALPHABET_SIZE = 26


def _random_key() -> str:
    """Generate a random key of lowercase letters."""
    return "".join(
        secrets.choice(string.ascii_lowercase) for _ in range(DEFAULT_KEY_LEN)
    )


class Cipher:
    """Vigenère cipher implementation for encoding and decoding text."""

    def __init__(self, key: str | None = None):
        """Initialize cipher with a key (generates random key if not provided)."""
        self._key = key if key else _random_key()
        self._key_len = len(self._key)

    @property
    def key(self) -> str:
        """Get the cipher key."""
        return self._key

    def _shift_at(self, i: int) -> int:
        """Get shift value for character at position i."""
        return ord(self._key[i % self._key_len]) - LOWERCASE_A_ORD

    def encode(self, plaintext: str) -> str:
        """Encode plaintext using the Vigenère cipher."""
        return "".join(
            _to_chr(_to_int(c) + self._shift_at(i)) for i, c in enumerate(plaintext)
        )

    def decode(self, ciphertext: str) -> str:
        """Decode ciphertext using the Vigenère cipher."""
        return "".join(
            _to_chr(_to_int(c) - self._shift_at(i)) for i, c in enumerate(ciphertext)
        )


def _to_int(c: str) -> int:
    """Convert lowercase letter to 0-based integer (a=0, b=1, etc.)."""
    return ord(c) - LOWERCASE_A_ORD


def _to_chr(n: int) -> str:
    """Convert integer to lowercase letter with wrapping (0=a, 1=b, etc.)."""
    return chr(LOWERCASE_A_ORD + n % ALPHABET_SIZE)
