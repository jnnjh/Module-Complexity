from typing import List, Tuple, Dict

change_cache: Dict[Tuple[int, int], int] = {}
def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    return ways_to_make_change_helper(total, [200, 100, 50, 20, 10, 5, 2, 1],0)


def ways_to_make_change_helper(total: int, coins: List[int], coin_index: int) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
   
   #If total is 0, we found exactly 1 valid way to make change
    if total == 0:
        return 1
        
    #If total becomes negative or we run out of coins, this way failed
    if total < 0 or coin_index >= len(coins):
        return 0

    # Cache check
    cache_key = (total, coin_index)
    if cache_key in change_cache:
        return change_cache[cache_key]

    current_coin = coins[coin_index]

    # 1 use the current coin and stay on the same coin index
    # 2 skip the current coin and move to the next coin index
    ways = (
        ways_to_make_change_helper(total - current_coin, coins, coin_index) +
        ways_to_make_change_helper(total, coins, coin_index + 1)
    )
       # store the result in the cache before the return      
    change_cache[cache_key] = ways
    return ways
