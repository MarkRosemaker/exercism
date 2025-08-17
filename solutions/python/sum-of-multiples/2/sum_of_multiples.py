from math import lcm

SIMPLE_SET_LIMIT_THRESHOLD = 2_000_000


def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """Return the sum of all unique multiples of given base values less than a limit.

    For each value in `multiples`, all positive multiples of that value that are
    strictly less than `limit` are considered. Duplicate multiples (numbers that
    are multiples of more than one base value) are only counted once.

    Parameters
    - limit: int
        The exclusive upper bound (level number). Only multiples < limit are
        included. Non-negative integer.
    - multiples: list[int]
        Sorted, unique list of base values (factors). Elements are non-negative
        integers.

    Returns
    - int
        Sum of all unique multiples of the provided base values that are less
        than `limit`.

    Example
    --------
    For `limit=20` and `multiples=[3, 5]` the function sums
    {3,5,6,9,10,12,15,18} -> 78.
    """
    # Heuristic: if the level `limit` is small enough, use the
    # straightforward set-based approach. This is a short, readable
    # comprehension that works well when `limit` is modest.
    # For large `limit` we fall back to inclusion-exclusion math to avoid
    # enumerating many values.
    if limit <= SIMPLE_SET_LIMIT_THRESHOLD:
        # One-liner set comprehension: skip n==0 (falsy) and collect all
        # multiples of n that are < limit; set removes duplicates.
        return sum({i for n in multiples if n for i in range(n, limit, n)})

    # Inclusion-exclusion path for large limits
    total = 0

    # Number of available base factors. We will iterate over every non-empty
    # subset of these factors using a bitmask. For num_factors factors there are
    # (2**num_factors - 1) non-empty subsets.
    num_factors = len(multiples)

    # Inclusion-exclusion via bitmask iteration with descriptive names:
    # - Each subset_mask (1 .. 2^num_factors - 1) represents a non-empty subset
    #   of indices in `multiples`.
    # - For each subset we compute:
    #     * `subset_size`: number of selected factors
    #     * `current_lcm`: least common multiple of selected factors
    # - Add `_sum_multiples_of(current_lcm, limit)` when subset_size is odd,
    #   subtract when even.
    for subset_mask in range(1, 1 << num_factors):
        # LCM identity: starting at 1 means the first selected factor becomes
        # the running LCM directly (lcm(1, x) == x for positive x).
        current_lcm = 1
        subset_size = 0

        # Build the LCM for the selected subset and count selected elements.
        for index in range(num_factors):
            if (subset_mask >> index) & 1:
                subset_size += 1
                # Use math.lcm for clarity and performance when available.
                # math.lcm returns 0 if any argument is 0, which naturally
                # yields zero contribution from such subsets.
                current_lcm = lcm(current_lcm, multiples[index])

        # Inclusion-exclusion: add for odd-sized subsets, subtract for even.
        if subset_size % 2:
            total += _sum_multiples_of(current_lcm, limit)
        else:
            total -= _sum_multiples_of(current_lcm, limit)

    return total


def _sum_multiples_of(k: int, limit: int) -> int:
    if k <= 0:
        return 0

    # Multiples of k that are < limit are: k, 2k, 3k, ..., mk where m:
    m = (limit - 1) // k

    # This is an arithmetic series with m terms, first term k and last term mk.
    # Sum of first m integers is m*(m+1)//2, so the sum of k,2k,...,mk is
    # k * (1 + 2 + ... + m) == k * m * (m + 1) // 2.
    # Using this closed form avoids looping and is O(1).
    return k * m * (m + 1) // 2
