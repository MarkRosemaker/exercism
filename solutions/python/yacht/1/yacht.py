from collections import Counter
from enum import Enum, auto


# Score categories.
class Category(Enum):
    YACHT = auto()
    ONES = auto()
    TWOS = auto()
    THREES = auto()
    FOURS = auto()
    FIVES = auto()
    SIXES = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    LITTLE_STRAIGHT = auto()
    BIG_STRAIGHT = auto()
    CHOICE = auto()


YACHT = Category.YACHT
ONES = Category.ONES
TWOS = Category.TWOS
THREES = Category.THREES
FOURS = Category.FOURS
FIVES = Category.FIVES
SIXES = Category.SIXES
FULL_HOUSE = Category.FULL_HOUSE
FOUR_OF_A_KIND = Category.FOUR_OF_A_KIND
LITTLE_STRAIGHT = Category.LITTLE_STRAIGHT
BIG_STRAIGHT = Category.BIG_STRAIGHT
CHOICE = Category.CHOICE


def score(dice: list[int], category: Category) -> int:
    """
    Calculate the score for a given dice roll and category in the Yacht game.

    Args:
        dice (list[int]): List of five dice values (1-6).
        category (Category): Scoring category.

    Returns:
        int: The score for the given dice and category.
    """
    match category:
        case Category.YACHT:
            # All five dice must show the same value
            return 50 if len(set(dice)) == 1 else 0
        case Category.ONES:
            # Score is the sum of dice showing 1
            return sum_of_face(dice, 1)
        case Category.TWOS:
            # Score is the sum of dice showing 2
            return sum_of_face(dice, 2)
        case Category.THREES:
            # Score is the sum of dice showing 3
            return sum_of_face(dice, 3)
        case Category.FOURS:
            # Score is the sum of dice showing 4
            return sum_of_face(dice, 4)
        case Category.FIVES:
            # Score is the sum of dice showing 5
            return sum_of_face(dice, 5)
        case Category.SIXES:
            # Score is the sum of dice showing 6
            return sum_of_face(dice, 6)
        case Category.FULL_HOUSE:
            # Only valid if there are exactly two distinct values, with counts 2 and 3
            counts = Counter(dice)
            return (
                sum(face * count for face, count in counts.items())
                if sorted(counts.values()) == [2, 3]
                else 0
            )
        case Category.FOUR_OF_A_KIND:
            # At least four dice showing the same face
            face, count = Counter(dice).most_common(1)[0]
            return face * 4 if count >= 4 else 0
        case Category.LITTLE_STRAIGHT:
            # Sequence 1-2-3-4-5
            return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
        case Category.BIG_STRAIGHT:
            # Sequence 2-3-4-5-6
            return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
        case Category.CHOICE:
            # Any combination, score is sum of all dice
            return sum(dice)
        case _:
            raise ValueError("unknown category")


def sum_of_face(dice: list[int], face: int) -> int:
    """
    Return the sum of all dice showing the given face value.

    Args:
        dice (list[int]): List of dice values.
        face (int): The face value to sum.

    Returns:
        int: The total for dice showing 'face'.
    """
    return sum(d for d in dice if d == face)
