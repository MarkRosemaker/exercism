SOUNDS = ((3, "Pling"), (5, "Plang"), (7, "Plong"))


def convert(number: int) -> str:
    """Converts a number into a string that contains raindrop sounds corresponding to certain potential factors.

    - If the number is divisible by 3, adds "Pling" to the result.
    - If the number is divisible by 5, adds "Plang" to the result.
    - If the number is divisible by 7, adds "Plong" to the result.
    - If the number is not divisible by 3, 5, or 7, returns the number as a string.

    Args:
        number (int): The number to be converted.

    Returns:
        str: The raindrop sounds or the number as a string.
    """
    # Collect the corresponding raindrop sounds for each factor that divides the number
    sounds = [sound for factor, sound in SOUNDS if number % factor == 0]
    return "".join(sounds) if sounds else str(number)
