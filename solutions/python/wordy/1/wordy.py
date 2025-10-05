import re
from typing import Callable

# Expected prefix for all valid questions
PREFIX = "What is "

# Dictionary mapping operation words to their corresponding functions
# Using lambda functions for concise mathematical operations
OPERATIONS: dict[str, Callable[[int, int], int]] = {
    "plus": lambda x, y: x + y,
    "minus": lambda x, y: x - y,
    "multiplied by": lambda x, y: x * y,
    "divided by": lambda x, y: x // y,  # Integer division
}

# Store addition operation for initial state handling
ADDITION = OPERATIONS["plus"]

# Regex to validate the overall question format
# Matches: "What is" followed by any combination of numbers and word operations, ending with "?"
re_question = re.compile(r"^What is( -?\d+| [a-z ]+)*\?$")

# Regex to extract tokens: numbers, known operations, or any word sequences
re_tokens = re.compile(
    rf"-?\d+|{r'|'.join(re.escape(op) for op in OPERATIONS.keys())}|[a-z]+(?:\s[a-z]+)*"
)

# Regex to identify if a token is a number (positive or negative integer)
re_number = re.compile(r"^-?\d+$")


def answer(question: str) -> int:
    """
    Parse and evaluate a word problem mathematical expression.

    Args:
        question: A string like "What is 5 plus 3?"

    Returns:
        The integer result of the mathematical expression

    Raises:
        ValueError: If the question format is invalid ("syntax error")
                   or contains unknown operations ("unknown operation")
    """
    # Validate the overall question format using regex
    match = re_question.match(question)
    if not match:
        raise ValueError("syntax error")

    # Extract the mathematical expression by removing "What is " and "?"
    expr = question[len(PREFIX) : -1]

    # Initialize result and operation state
    # Start with result=0 and addition operation to handle the first number
    res: int = 0
    op: Callable[[int, int], int] | None = ADDITION

    # Process each token in the expression
    for el in re_tokens.findall(expr):
        is_number = re_number.match(el) is not None

        # State validation: we should alternate between operations and numbers
        if is_number != (op is not None):
            raise ValueError("syntax error")

        if is_number:
            # Apply the pending operation and clear it
            res = op(res, int(el))  # type: ignore (op is guaranteed to be not None here)
            op = None
        else:
            # Current token should be an operation
            if el not in OPERATIONS:
                raise ValueError("unknown operation")
            op = OPERATIONS[el]

    # If we end with a pending operation, it means the expression was incomplete
    if op:
        raise ValueError("syntax error")

    return res
