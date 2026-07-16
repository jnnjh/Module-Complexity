from typing import List

cache = {}

def ways_to_make_change(total: int) -> int:
    return ways_to_make_change_helper(total, (200, 100, 50, 20, 10, 5, 2, 1))

def ways_to_make_change_helper(total: int, coins) -> int:
    key = (total, coins)
    if key in cache:
        return cache[key]
    
    if total == 0:
        return 1
    if len(coins) == 0:
        return 0

    ways = 0
    coin = coins[0]
    for count in range(total // coin + 1):
        intermediate = ways_to_make_change_helper(total - coin * count, coins[1:])
        ways += intermediate
    
    cache[key] = ways
    return ways
