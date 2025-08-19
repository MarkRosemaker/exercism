def two_fer(name: str = "you") -> str:
    """
    Return the 'two-fer' phrase for the given name.

    If a name is provided, returns "One for {name}, one for me.".
    If no name is provided the function defaults to "you".

    Examples:
        two_fer("Alice") -> "One for Alice, one for me."
        two_fer()        -> "One for you, one for me."
    """

    return f"One for {name}, one for me."
