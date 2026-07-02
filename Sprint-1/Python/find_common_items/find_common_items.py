from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n^3)
    Space Complexity:O(min(n,m))
    Optimal time complexity: O(n+m)
    """
    
    first_set = set(first_sequence)
    second_set = set(second_sequence)
    # we use the & operator shortcut, of The intersection() method 
    # to return a set that contains the similarity between two or more sets
    common_items= first_set & second_set
    return list(common_items)

print(find_common_items([1,3,5,4],[1,4,8,0]))
