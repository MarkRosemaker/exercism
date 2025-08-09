def find(search_list: list[int], value: int):
    """
    Performs a binary search on a sorted list to find the index of a given value.

    Args:
        search_list (list[int]): A sorted list of integers to search.
        value (int): The integer value to find in the list.

    Returns:
        int: The index of the value in the list.

    Raises:
        ValueError: If the value is not present in the list.
    """
    left, right = 0, len(search_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if search_list[middle] < value:
            # If the middle element is less than our item, we can eliminate that element and all the elements before it.
            left = middle + 1
        elif search_list[middle] > value:
            # If the middle element is greater than our item, we can eliminate that element and all the elements after it.
            right = middle - 1
        else:
            return middle

    raise ValueError("value not in array")
