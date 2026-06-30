from typing import List

cache = {}

def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    ways = [0] * (total + 1)
    ways[0] = 1
    
    for coin in coins:
        for amount in range(coin, total + 1):
            ways[amount] += ways[amount - coin]    
    
    
    return ways[total]


def ways_to_make_change_helper(total: int, coins: List[int], coin_start_index: int = 0) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    if total == 0:
        return 1
    if total < 0 or coin_start_index >= len(coins):
        return 0

    memo_key = (total, coin_start_index)
    if memo_key in cache:
        return cache[memo_key]

    coin = coins[coin_start_index]
    ways = ways_to_make_change_helper(total, coins, coin_start_index + 1)
    if coin <= total:
        ways += ways_to_make_change_helper(total - coin, coins, coin_start_index)

    cache[memo_key] = ways
    return ways
