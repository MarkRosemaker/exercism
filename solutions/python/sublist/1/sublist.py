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
    if len(list_one) == len(list_two):
        if list_one == list_two:
            return EQUAL
        else:
            return UNEQUAL
    elif len(list_one) < len(list_two):
        # Checking if list_one is a SUBLIST of list_two
        return sublist_helper(list_one, list_two)
    else:
        # Checking if list_one is a SUPERLIST of list_two
        return sublist_helper(list_two, list_one, is_swapped=True)


def sublist_helper(
    shorter: list[int], longer: list[int], is_swapped: bool = False
) -> int:
    """
    Helper function to determine if 'shorter' is a contiguous sublist (slice) of 'longer'.

    If 'shorter' is empty, it is considered a sublist at every possible position in 'longer' (i.e., the function will check all slices of length zero, which always match).

    Args:
        shorter (list[int]): The shorter list to check as a sublist.
        longer (list[int]): The longer list to check within.
        is_swapped (bool): If True, indicates that the original call was for SUPERLIST; otherwise, SUBLIST.

    Returns:
        int: SUPERLIST, SUBLIST, or UNEQUAL.
    """
    stop = len(longer) - len(shorter) + 1
    for i in range(stop):
        if shorter == longer[i : i + len(shorter)]:
            return SUPERLIST if is_swapped else SUBLIST

    return UNEQUAL
