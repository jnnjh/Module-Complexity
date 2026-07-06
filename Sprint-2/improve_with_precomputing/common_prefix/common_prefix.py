from typing import List


def find_longest_common_prefix(strings: List[str]):
    """
    find_longest_common_prefix returns the longest string common at the start of any two strings in the passed list.

    In the event that an empty list, a list containing one string, or a list of strings with no common prefixes is passed, the empty string will be returned.
    """

    if len(strings) < 2:
        return ""
    
    # Sorting first (O(n log n * k)) means the longest common prefix between
    # ANY two strings in the list is guaranteed to be between two ADJACENT
    # strings after sorting. This lets us check only n-1 adjacent pairs
    # instead of comparing every pair (O(n^2 * k) in the original version),
    # reducing the overall complexity to O(n log n * k).
    
    strings = sorted(strings)
    
    longest = ""

    for i in range(len(strings) - 1):
        common = find_common_prefix(strings[i], strings[i + 1])
        if len(common) > len(longest):
            longest = common
    return longest


def find_common_prefix(left: str, right: str) -> str:
    min_length = min(len(left), len(right))
    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]
    return left[:min_length]
