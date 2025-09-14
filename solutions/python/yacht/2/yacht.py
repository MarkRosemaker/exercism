from collections import Counter
from collections.abc import Callable


def YACHT(dice: list[int]) -> int:
    # All five dice must show the same value
    return 50 if len(set(dice)) == 1 else 0


def ONES(dice: list[int]):
    # Score is the sum of dice showing 1
    return sum_of_face(dice, 1)


def TWOS(dice: list[int]) -> int:
    # Score is the sum of dice showing 2
    return sum_of_face(dice, 2)


def THREES(dice: list[int]) -> int:
    # Score is the sum of dice showing 3
    return sum_of_face(dice, 3)


def FOURS(dice: list[int]) -> int:
    # Score is the sum of dice showing 4
    return sum_of_face(dice, 4)


def FIVES(dice: list[int]) -> int:
    # Score is the sum of dice showing 5
    return sum_of_face(dice, 5)


def SIXES(dice: list[int]) -> int:
    # Score is the sum of dice showing 6
    return sum_of_face(dice, 6)


def FULL_HOUSE(dice: list[int]) -> int:
    # Only valid if there are exactly two distinct values, with counts 2 and 3
    counts = Counter(dice)
    return (
        sum(face * count for face, count in counts.items())
        if sorted(counts.values()) == [2, 3]
        else 0
    )


def FOUR_OF_A_KIND(dice: list[int]) -> int:
    # At least four dice showing the same face
    face, count = Counter(dice).most_common(1)[0]
    return face * 4 if count >= 4 else 0


def LITTLE_STRAIGHT(dice: list[int]) -> int:
    # Sequence 1-2-3-4-5
    return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0


def BIG_STRAIGHT(dice: list[int]) -> int:
    # Sequence 2-3-4-5-6
    return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0


def CHOICE(dice: list[int]) -> int:
    # Any combination, score is sum of all dice
    return sum(dice)


def score(dice: list[int], category: Callable[[list[int]], int]) -> int:
    """
    Calculate the score for a given dice roll and category lambda in the Yacht game.

    Args:
        dice (list[int]): List of five dice values (1-6).
        category (Callable[[list[int]], int]): Scoring function.

    Returns:
        int: The score for the given dice and category.
    """
    return category(dice)


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
