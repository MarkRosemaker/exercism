def response(hey_bob: str) -> str:
    """
    Generate Bob's response to a given remark.

    Bob only ever answers one of five things:

    - "Sure." This is his response if you ask him a question, such as "How are you?"
    - "Whoa, chill out!" This is his answer if you YELL AT HIM.
    - "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
    - "Fine. Be that way!" This is how he responds to silence.
    - "Whatever." This is what he answers to anything else.

    Args:
        hey_bob (str): The remark directed at Bob.

    Returns:
        str: Bob's response based on the remark.
    """
    # Remove leading and trailing whitespace from the input
    hey_bob = hey_bob.strip()

    if not hey_bob:
        return "Fine. Be that way!"

    is_question = hey_bob.endswith("?")
    is_yelling = any(c.isalpha() for c in hey_bob) and hey_bob.isupper()

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever."  # Default response for anything else
