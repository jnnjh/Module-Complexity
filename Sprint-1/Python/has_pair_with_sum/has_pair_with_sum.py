from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(n²)
    Space Complexity: O(1)
    Optimal Time Complexity: O(n)

    Analysis:
    - The original implementation uses nested loops to compare every
      possible pair of numbers.
    - This results in O(n²) time complexity.
    - The complexity can be reduced by using a set to store previously
      seen numbers. For each number, calculate its complement
      (target_sum - number) and check if it already exists in the set.

    Refactored Complexity:
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    """

    seen = set()

    for number in numbers:
        complement = target_sum - number

        if complement in seen:
            return True

        seen.add(number)

    return False