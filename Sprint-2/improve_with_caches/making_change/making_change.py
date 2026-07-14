from typing import List

COINS = [200, 100, 50, 20, 10, 5, 2, 1]


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200,
    returns a count of all of the ways to make the passed total value.
    """
    cache = {}

    def helper(total: int, start_index: int) -> int:
        key = (total, start_index)

        if key in cache:
            return cache[key]

        if total == 0 or start_index >= len(COINS):
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
                    ways += helper(
                        total - total_from_coins,
                        coin_index + 1
                    )

                count_of_coin += 1

        cache[key] = ways
        return ways

    return helper(total, 0)