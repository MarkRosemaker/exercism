SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one: list[int], list_two: list[int]) -> int:
    """
    Determine the relationship between two lists: whether the first list is equal to, a sublist of, a superlist of, or unequal to the second list.

    Note: This function only checks for contiguous sublists (i.e., slices), not general subsequences.

    Given two lists, list_one and list_two, this function compares them and returns a constant indicating their relationship:
    - EQUAL: if both lists contain the same elements in the same order.
    - SUBLIST: if list_one is a contiguous sub-sequence (slice) of list_two.
    - SUPERLIST: if list_two is a contiguous sub-sequence (slice) of list_one.
    - UNEQUAL: if none of the above conditions are met.

    Args:
        list_one (list[int]): The first list to compare.
        list_two (list[int]): The second list to compare.

    Returns:
        int: One of the constants EQUAL, SUBLIST, SUPERLIST, or UNEQUAL, indicating the relationship between the two lists.

    Examples:
        sublist([], []) -> EQUAL
        sublist([1, 2, 3], []) -> SUPERLIST
        sublist([], [1, 2, 3]) -> SUBLIST
        sublist([1, 2, 3], [1, 2, 3, 4, 5]) -> SUBLIST
        sublist([3, 4, 5], [1, 2, 3, 4, 5]) -> SUBLIST
        sublist([1, 2, 3], [1, 2, 3]) -> EQUAL
        sublist([1, 2, 3, 4, 5], [2, 3, 4]) -> SUPERLIST
        sublist([1, 2, 4], [1, 2, 3, 4, 5]) -> UNEQUAL
        sublist([1, 2, 3], [1, 3, 2]) -> UNEQUAL
    """
    if list_one == list_two:
        return EQUAL
    if is_sublist(list_one, list_two):
        return SUBLIST
    if is_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL


def is_sublist(shorter: list[int], longer: list[int]) -> bool:
    """
    Determines whether the first list (`shorter`) is a contiguous sublist of the second list (`longer`).

    Args:
        shorter (list[int]): The list to check as a potential sublist.
        longer (list[int]): The list to search within.

    Returns:
        bool: True if `shorter` is a contiguous sublist of `longer`, False otherwise.
    """
    n, m = len(shorter), len(longer)
    stop = m - n + 1
    for i in range(stop):
        if longer[i : i + n] == shorter:
            return True
    return False
