def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """Find the minimum number of coins that sum to the target amount.

    Args:
        coins: Available coin denominations
        target: Target amount to make change for

    Returns:
        List of coins that sum to target using fewest coins possible

    Raises:
        ValueError: If target is negative or cannot be made with given coins

    Examples:
        >>> find_fewest_coins([1, 5, 10, 25], 15)
        [5, 10]
        >>> find_fewest_coins([1, 5, 10, 25], 40)
        [5, 10, 25]
    """
    if target < 0:
        raise ValueError("target can't be negative")

    # Exit early if target is zero
    if target == 0:
        return []

    # Filter out coins larger than target
    coins = [coin for coin in coins if coin <= target]

    INF = target + 1

    # num_coins[i] = minimum number of coins needed to make amount i
    # Use target + 1 to represent impossible or unknown amounts
    num_coins: list[int] = [INF] * (target + 1)
    num_coins[0] = 0

    # parent[i] = the coin used to reach amount i with minimum coins
    parent: list[int] = [-1] * (target + 1)

    # Build up the solution using DFS-like approach with stack
    stack = [0]
    while stack:
        amount = stack.pop()

        # Try adding each coin to the current amount
        for coin in coins:
            next_amount = amount + coin
            if next_amount > target:
                break  # Stop loop, coins are getting too big

            next_num = num_coins[amount] + 1
            if next_num >= num_coins[next_amount]:
                continue  # Already have better or equal solution

            num_coins[next_amount] = next_num
            parent[next_amount] = coin

            # Add to stack for further exploration
            stack.append(next_amount)

    # If target amount is impossible to make
    if num_coins[target] == INF:
        raise ValueError("can't make target with given coins")

    # Reconstruct the solution
    result: list[int] = []
    current = target
    while current > 0:
        coin = parent[current]
        result.append(coin)
        current -= coin

    return result
