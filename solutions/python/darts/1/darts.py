INNER_RADIUS = 1
MIDDLE_RADIUS = 5
OUTER_RADIUS = 10

INNER_RADIUS_SQ = INNER_RADIUS**2
MIDDLE_RADIUS_SQ = MIDDLE_RADIUS**2
OUTER_RADIUS_SQ = OUTER_RADIUS**2


def score(x: float, y: float) -> int:
    """
    Calculate the points scored in a single toss of a Darts game.

    Given the Cartesian coordinates (x, y) of a dart landing on a concentric target centered at (0, 0),
    returns the score based on the distance from the center:

    - 10 points: dart lands within the inner circle (radius <= 1).
    - 5 points: dart lands within the middle circle (1 < radius <= 5).
    - 1 point: dart lands within the outer circle (5 < radius <= 10).
    - 0 points: dart lands outside the target (radius > 10).

    Parameters:
        x (float): The x-coordinate of the dart's landing position.
        y (float): The y-coordinate of the dart's landing position.

    Returns:
        int: The score earned for the dart's position.
    """

    # Use squared distance to avoid the cost of a square root operation.
    dist_sq = x**2 + y**2
    if dist_sq > OUTER_RADIUS_SQ:
        return 0
    if dist_sq > MIDDLE_RADIUS_SQ:
        return 1
    if dist_sq > INNER_RADIUS_SQ:
        return 5
    return 10
