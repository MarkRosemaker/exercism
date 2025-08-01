def triangle(sides: list[int]) -> bool:
    """
    Checks if the given list of sides can form a valid triangle.

    A valid triangle must have exactly three positive integer sides,
    and the sum of any two sides must be greater than the third side.

    Parameters:
        sides (list[int]): A list of three positive integers representing the side lengths.

    Returns:
        bool: True if the sides can form a triangle, False otherwise.
    """
    if len(sides) != 3 or any(side <= 0 for side in sides):
        return False

    a, b, c = sides
    return a + b > c and b + c > a and a + c > b


def equilateral(sides: list[int]) -> bool:
    """
    Checks if the given list of sides can form an equilateral triangle.

    An equilateral triangle has all three sides of equal length.

    Parameters:
        sides (list[int]): A list of three positive integers representing the side lengths.

    Returns:
        bool: True if the sides can form an equilateral triangle, False otherwise.
    """
    return triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list[int]) -> bool:
    """
    Checks if the given list of sides can form an isosceles triangle.

    An isosceles triangle has at least two sides of equal length.

    Parameters:
        sides (list[int]): A list of three positive integers representing the side lengths.

    Returns:
        bool: True if the sides can form an isosceles triangle, False otherwise.
    """
    return triangle(sides) and len(set(sides)) <= 2


def scalene(sides: list[int]) -> bool:
    """
    Checks if the given list of sides can form a scalene triangle.

    A scalene triangle has all sides of different lengths.

    Parameters:
        sides (list[int]): A list of three positive integers representing the side lengths.

    Returns:
        bool: True if the sides can form a scalene triangle, False otherwise.
    """
    return triangle(sides) and len(set(sides)) == 3
