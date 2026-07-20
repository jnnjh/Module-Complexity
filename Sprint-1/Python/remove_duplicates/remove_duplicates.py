from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time Complexity: O(n²)
    Space Complexity: O(n)
    Optimal Time Complexity: O(n)

    Analysis:
    - The original implementation uses nested loops.
    - For each value, it searches through the list of unique items
      to determine whether it has already been seen.
    - This results in O(n²) time complexity in the worst case.
    - The complexity can be reduced by using a set to track values
      that have already been seen. Set lookups are O(1) on average,
      while the list preserves the order of first occurrence.

    Refactored Complexity:
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    """

    seen = set()
    unique_items: List[ItemType] = []

    for value in values:
        if value not in seen:
            seen.add(value)
            unique_items.append(value)

    return unique_items