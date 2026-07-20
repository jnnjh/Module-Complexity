from typing import List, Tuple

cache = {}


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200,
    returns the number of ways to make the passed total value.
    """
    cache.clear()
    return ways_to_make_change_helper(
        total, (200, 100, 50, 20, 10, 5, 2, 1)
    )


def ways_to_make_change_helper(total: int, coins: Tuple[int, ...]) -> int:
    key = (total, coins)

    if key in cache:
        return cache[key]

    if total == 0:
        return 1

    if total < 0 or len(coins) == 0:
        return 0

    ways = 0

    coin = coins[0]
    remaining = coins[1:]

    amount = total
    while amount >= 0:
        ways += ways_to_make_change_helper(amount, remaining)
        amount -= coin

    cache[key] = ways
    return ways