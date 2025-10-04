from collections import Counter
from enum import IntEnum
from functools import total_ordering


def best_hands(hands: list[str]) -> list[str]:
    """Return the best poker hand(s) from a list of hands.

    Args:
        hands: List of poker hands as strings (e.g., ["4S 5H 6C 7D 8S"])

    Returns:
        List of the best hand(s) as strings. Multiple hands returned if tied.
    """
    if not hands:
        return []

    # Start with the first hand as the current best,
    # then compare each remaining hand to the current best
    best: list[Hand] = [Hand(hands[0])]
    for hand in hands[1:]:
        h = Hand(hand)
        if best[0] < h:
            best = [h]
        elif not (h < best[0]):  # tie
            best.append(h)

    return [str(hand) for hand in best]


class Category(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9


class Rank(int):
    """Custom int subclass for card ranks with string parsing and display.

    Ranks: 2-10 (numeric), J=11, Q=12, K=13, A=14
    """

    def __new__(cls, rank_str: str) -> int:
        # Convert string representation to numeric value
        value = Rank._from_str(rank_str)
        if not (2 <= value <= 14):
            raise ValueError(f"Invalid rank: {value}")
        return super().__new__(cls, value)

    @staticmethod
    def _from_str(s: str) -> int:
        """Convert string rank to numeric value."""
        if s.isdigit():
            return int(s)
        match s:
            case "J":
                return 11
            case "Q":
                return 12
            case "K":
                return 13
            case "A":
                return 14
            case _:
                raise ValueError(f"Invalid rank: {s}")

    def __str__(self) -> str:
        """Convert numeric rank back to string representation."""
        match self:
            case 11:
                return "J"
            case 12:
                return "Q"
            case 13:
                return "K"
            case 14:
                return "A"
            case _:
                # For ranks 2-10, use the numeric value
                return super().__str__()


ACE = Rank("A")

# A-2-3-4-5 straight (wheel) - Ace plays low
WHEEL_STRAIGHT = [ACE, 5, 4, 3, 2]


@total_ordering
class Hand:
    """Represents a poker hand with comparison and categorization logic."""

    _NUM_CARDS = 5

    def __init__(self, s: str) -> None:
        # Parse the hand string into individual cards
        cards = [Card(c) for c in s.split()]
        if len(cards) != self._NUM_CARDS:
            raise ValueError(
                f"Hand must have exactly {Hand._NUM_CARDS} cards, got {len(cards)}"
            )

        self._s = s  # Store original string for __str__

        # Sort cards by rank (highest first) for easier comparison
        self._cards: list[Card] = sorted(cards, reverse=True)
        self._ranks: list[int] = [c.rank for c in self._cards]

        # Count occurrences of each rank for pattern detection
        self._rank_counts = Counter(self._ranks).most_common()
        self.most_common_rank, self.most_common_count = self._rank_counts[0]

    @property
    def pairs(self) -> list[int]:
        """Return ranks that appear exactly twice, sorted high to low."""
        return sorted(
            [rank for rank, count in self._rank_counts if count == 2], reverse=True
        )

    @property
    def triple(self) -> int:
        """Return the rank that appears three times, or 0 if none."""
        return self.most_common_rank if self.most_common_count == 3 else 0

    @property
    def quad(self) -> int:
        """Return the rank that appears four times, or 0 if none."""
        return self.most_common_rank if self.most_common_count == 4 else 0

    @property
    def kicker(self) -> int:
        """Return the card rank of the kicker (the single remaining card) for four-of-a-kind hands."""
        return self._rank_counts[1][0] if self.most_common_count == 4 else 0

    @property
    def category(self) -> Category:
        """The poker hand category (pair, straight, etc.)."""

        # Check for patterns based on rank counts first (most common cases)
        if self.quad:
            return Category.FOUR_OF_A_KIND
        if self.triple and self.pairs:
            return Category.FULL_HOUSE
        if self.triple:
            return Category.THREE_OF_A_KIND
        if len(self.pairs) == 2:
            return Category.TWO_PAIRS
        if len(self.pairs) == 1:
            return Category.ONE_PAIR

        # Check for flush and straight (require all 5 cards to match patterns)
        suit = self._cards[0].suit
        same_suit = all(suit == c.suit for c in self._cards[1:])

        if same_suit:
            if self._is_straight:
                return Category.STRAIGHT_FLUSH
            else:
                return Category.FLUSH
        elif self._is_straight:
            return Category.STRAIGHT

        # No special patterns found
        return Category.HIGH_CARD

    @property
    def _is_straight(self) -> bool:
        """Check if cards form a sequence (straight)."""
        return (
            # Normal straight: each card 1 less than previous (cards sorted high to low)
            all(
                self._ranks[i] - 1 == self._ranks[i + 1]
                for i in range(Hand._NUM_CARDS - 1)
            )
            # Check for special case: A-2-3-4-5 (wheel/bicycle straight)
            or self._is_wheel
        )

    @property
    def _is_wheel(self) -> bool:
        """Check if this is a wheel straight (A-2-3-4-5).

        In this special straight, Ace plays low (as 1).
        """
        return self._ranks == WHEEL_STRAIGHT

    def __str__(self) -> str:
        return self._s

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented

        # First compare by hand category (straight flush > four of a kind > etc.)
        category = self.category
        if category != other.category:
            return self.category < other.category

        # Same category - need to compare within category
        match category:
            case Category.STRAIGHT_FLUSH | Category.STRAIGHT:
                # Wheel straight (A-2-3-4-5) loses to any other straight
                self_is_wheel = self._is_wheel
                if self_is_wheel is not other._is_wheel:
                    return self_is_wheel
            case Category.FOUR_OF_A_KIND:
                # Compare the rank of the four cards first
                if self.quad != other.quad:
                    return self.quad < other.quad
                # If same quad rank, compare kickers
                return self.kicker < other.kicker
            case Category.FULL_HOUSE:
                # Compare triple first, then pair
                return (
                    self.triple < other.triple
                    if self.triple != other.triple
                    else self.pairs[0] < other.pairs[0]
                )
            case Category.FLUSH:
                # Tie-breaking for flush is handled by comparing card ranks below
                pass
            case Category.THREE_OF_A_KIND:
                # Compare the rank of the three cards
                if self.triple != other.triple:
                    return self.triple < other.triple
            case Category.ONE_PAIR | Category.TWO_PAIRS:
                # Compare pairs from highest to lowest
                for self_pair, other_pair in zip(self.pairs, other.pairs):
                    if self_pair != other_pair:
                        return self_pair < other_pair
            case _:
                # HIGH_CARD case - fall through to card comparison
                pass

        # Tie-breaker: compare cards from highest to lowest
        for i in range(Hand._NUM_CARDS):
            if self._cards[i] == other._cards[i]:
                continue
            return self._cards[i] < other._cards[i]

        # Hands are identical
        return False

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        return not (self < other) and not (other < self)


@total_ordering
class Card:
    """Represents a playing card with rank and suit.

    Cards are ordered by rank only (2 < 3 < ... < J < Q < K < A).
    """

    def __init__(self, s: str) -> None:
        if len(s) < 2:
            raise ValueError(f"Invalid card format: {s}")

        # Parse rank (all characters except the last) and suit (last character)
        self.rank = Rank(s[:-1])
        self.suit = s[-1]

        if self.suit not in "CDHS":
            raise ValueError(f"Invalid suit: {self.suit}")

    def __str__(self) -> str:
        return str(self.rank) + self.suit

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented

        # Cards are compared by rank only (suit doesn't matter for poker hand ranking)
        return self.rank < other.rank

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented

        # Cards are equal if they have the same rank (suit doesn't matter)
        return self.rank == other.rank
