from typing import Any, Callable


def append(list1: list[Any], list2: list[Any]) -> list[Any]:
    """
    Add all items in the second list to the end of the first list.

    Args:
        list1: The list to which items will be appended.
        list2: The list whose items will be added to list1.
    Returns:
        The modified list1 with all items from list2 appended.
    """
    # Alternative implementations:
    # - Use list1.extend(list2) for in-place extension (most idiomatic, but uses built-in).
    # - Return a new list: return list1 + list2 (creates a new list, not in-place).
    # - Use slice assignment: list1[len(list1):] = list2
    for el in list2:
        list1.append(el)
    return list1


def concat(lists: list[list[Any]]) -> list[Any]:
    """
    Combine all items in a series of lists into one flattened list.

    Args:
        lists: A list of lists to concatenate.
    Returns:
        A single list containing all items from the input lists.
    """
    # Alternative implementations:
    # - List comprehension: [el for lst in lists for el in lst]
    # - Using sum: sum(lists, []) (not recommended for large lists)
    # - Using itertools.chain: list(itertools.chain.from_iterable(lists))
    res: list[Any] = []
    for lst in lists:
        res = append(res, lst)
    return res


def filter(function: Callable[[Any], bool], lst: list[Any]) -> list[Any]:
    """
    Return a list of all items for which the predicate function returns True.

    Args:
        function: A predicate function that returns True or False for an item.
        my_list: The list to filter.
    Returns:
        A list of items for which function(item) is True.
    """
    # Alternative implementations:
    # - List comprehension: [el for el in lst if function(el)]
    # - Using built-in filter: list(filter(function, lst))
    result: list[Any] = []
    for el in lst:
        if function(el):
            result.append(el)
    return result


def length(list: list[Any]) -> int:
    """
    Return the total number of items in the list.

    Args:
        list: The list whose length is to be determined.
    Returns:
        The number of items in the list.
    """
    # Alternative implementations:
    # - Built-in: return len(list)
    # - Using sum: return sum(1 for _ in list)

    # Manual count:
    count = 0
    for _ in list:
        count += 1
    return count


def map(function: Callable[[Any], Any], lst: list[Any]) -> list[Any]:
    """
    Return a list of the results of applying function(item) on all items.

    Args:
        function: A function to apply to each item in the list.
        list: The list whose items will be mapped.
    Returns:
        A list of results after applying function to each item.
    """
    # Alternative implementations:
    # - List comprehension: return [function(el) for el in list]
    # - Using built-in map: return list(map(function, list))
    result: list[Any] = []
    for el in lst:
        result.append(function(el))
    return result


def foldl(function: Callable[[Any, Any], Any], list: list[Any], initial: Any) -> Any:
    """
    Fold (reduce) each item into the accumulator from the left.

    Args:
        function: A function of two arguments (accumulator, item).
        list: The list to fold.
        initial: The initial accumulator value.
    Returns:
        The final accumulated value after folding from the left.
    """
    # Alternative implementations:
    # - Using functools.reduce: return functools.reduce(function, list, initial)
    result = initial
    for item in list:
        result = function(result, item)
    return result


def foldr(function: Callable[[Any, Any], Any], list: list[Any], initial: Any) -> Any:
    """
    Fold (reduce) each item into the accumulator from the right.

    Args:
        function: A function of two arguments (item, accumulator).
        list: The list to fold.
        initial: The initial accumulator value.
    Returns:
        The final accumulated value after folding from the right.
    """
    # Alternative implementations:
    # - Recursive: if not list: return initial; else: return function(list[0], foldr(function, list[1:], initial))
    # - Using functools.reduce with reversed: functools.reduce(lambda acc, x: function(x, acc), reversed(list), initial)
    result = initial
    start = length(list) - 1
    for i in range(start, -1, -1):
        result = function(result, list[i])
    return result


def reverse(input: list[Any]) -> list[Any]:
    """
    Return a list with all the original items, but in reversed order.

    Args:
        input: The list to reverse.
    Returns:
        A new list with the items in reverse order.
    """
    # Alternative implementations:
    # - Using slicing: return input[::-1]
    # - Using reversed: return list(reversed(input))
    # - Manual loop: result = []; for i in range(len(input)-1, -1, -1): result.append(input[i]); return result

    n = length(input)
    result = [None] * n
    for i in range(n):
        result[i] = input[n - i - 1]
    return result
