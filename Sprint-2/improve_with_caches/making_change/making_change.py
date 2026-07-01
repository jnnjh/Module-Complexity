from typing import List, Dict, Tuple

# 1. Create the cache
memo: Dict[Tuple[int, int], int] = {}

def ways_to_make_change_helper(total: int, coins: List[int]) -> int:
    # Cache Key
    state_key = (total, len(coins))

    # Cache Check
    if state_key in memo:
        return memo[state_key]

    if total == 0:
        return 1  
    if total < 0 or len(coins) == 0:
        return 0

    ways = 0
    # We take the first coin and pass the rest
    coin = coins[0]
    remaining_coins = coins[1:]

    count_of_coin = 0
    while (coin * count_of_coin) <= total:
        total_from_coins = total - (coin * count_of_coin)
        
        intermediate = ways_to_make_change_helper(total_from_coins, remaining_coins)
        ways += intermediate
        
        count_of_coin += 1
    
    # Store Result
    memo[state_key] = ways
    return ways

def ways_to_make_change(total: int) -> int:
    """Wrapper that matches the legacy test suite signature."""
    memo.clear() 
   
    default_coins = [200, 100, 50, 20, 10, 5, 2, 1]
    return ways_to_make_change_helper(total, default_coins)