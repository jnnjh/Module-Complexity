from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity:O(n^2)
    Space complexity:O(n)
    Optimal time complexity:O(n)
    """

   
    # dict.fromkeys creates a dictionary with values as keys,and automatically remove duplicates
    #list() to keep the original order.
    return list(dict.fromkeys(values))
print(remove_duplicates([1,2,2,3,3,4,0,0]))
