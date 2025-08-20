def square_root(number: int) -> int:
    """
    Calculate the integer square root of a given positive whole number using Newton's method.

    This function finds the square root of the input number, defined as the positive integer
    that, when multiplied by itself, equals the input number. It does not use any built-in
    math libraries or functions, and only handles cases where the result is a positive whole number.

    Parameters:
        number (int): A positive whole number whose square root is to be calculated.

    Returns:
        int: The positive integer square root of the input number.

    Note:
        - The function assumes that the input number is a perfect square.
        - The implementation uses Newton's (Heron's) method for successive approximation.
    """
    # Start with an initial guess for the square root
    guess = number
    while True:
        # Compute a new approximation using Newton's method
        new_guess = (guess + number // guess) // 2

        # If the new approximation is not less than the previous, we've converged
        if new_guess >= guess:
            return guess

        # Update the guess for the next iteration
        guess = new_guess
