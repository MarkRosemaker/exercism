def proverb(*inputs: str, qualifier: str | None) -> list[str]:
    """
    Generate a proverb based on a sequence of items, following the pattern:
    "For want of a {item} the {next_item} was lost." for each consecutive pair,
    and ending with "And all for the want of a {qualifier} {first_item}." if a qualifier is provided,
    or "And all for the want of a {first_item}." otherwise.

    Args:
        *inputs (str): A variable number of strings representing the items in the proverb.
        qualifier (str | None): An optional qualifier to prepend to the final item in the closing line.

    Returns:
        list[str]: A list of strings, each representing a line of the proverb.

    Example:
        proverb("nail", "shoe", "horse", qualifier="horseshoe")
        # [
        #   "For want of a nail the shoe was lost.",
        #   "For want of a shoe the horse was lost.",
        #   "And all for the want of a horseshoe nail."
        # ]
    """
    # If no inputs are provided, return an empty list
    if not inputs:
        return []

    # Generate the main proverb lines for each consecutive pair of items
    res = [f"For want of a {a} the {b} was lost." for a, b in zip(inputs, inputs[1:])]

    # Construct the final line, optionally including the qualifier
    res.append(
        f"And all for the want of a {qualifier + ' ' if qualifier else ''}{inputs[0]}."
    )
    return res
