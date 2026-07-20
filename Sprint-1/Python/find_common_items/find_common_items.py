from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n × m)
    Space Complexity: O(n)
    Optimal Time Complexity: O(n + m)

    Analysis:
    - The original implementation uses nested loops to compare every
      element in the first sequence with every element in the second.
    - It also checks `i not in common_items`, which performs another
      linear search.
    - The complexity can be reduced by converting the second sequence
      to a set for O(1) average lookups and using another set to
      prevent duplicate results.

    Refactored Complexity:
    - Time Complexity: O(n + m)
    - Space Complexity: O(n)
    """

    second_set = set(second_sequence)
    seen = set()
    common_items: List[ItemType] = []

    for item in first_sequence:
        if item in second_set and item not in seen:
            seen.add(item)
            common_items.append(item)

    return common_items