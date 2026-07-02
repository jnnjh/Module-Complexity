from typing import List
COINS = [200, 100, 50, 20, 10, 5, 2, 1]

cache = {}

def ways_to_make_change(total: int) -> int:
    return ways_to_make_change_helper(total, 0)


def ways_to_make_change_helper(total: int, start_index: int) -> int:
    key = (total, start_index)

    if key in cache:
        return cache[key]

    if total == 0:
        return 1

    if total < 0 or start_index >= len(COINS):
        return 0

    ways = 0
    for coin_index in range(start_index, len(COINS)):
        coin = COINS[coin_index]
        count_of_coin = 1
        while coin * count_of_coin <= total:
            total_from_coins = coin * count_of_coin
            if total_from_coins == total:
                ways += 1
            else:
                ways += ways_to_make_change_helper(
                    total - total_from_coins,
                    coin_index + 1
                )
            count_of_coin += 1

    cache[key] = ways
    return ways