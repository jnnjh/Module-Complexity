from typing import List


def find_longest_common_prefix(strings: List[str]):
    """
    find_longest_common_prefix returns the longest string common at the start of any two strings in the passed list.

    In the event that an empty list, a list containing one string, or a list of strings with no common prefixes is passed, the empty string will be returned.
    """
        if len(strings) < 2:
            return ""

        sorted_strings = sorted(strings)
        first = sorted_strings[0]
        last = sorted_strings[-1]
        min_length = min(len(first), len(last))
        i = 0
        while i < min_length and first[i] == last[i]:
            i += 1
        return first[:i]


def find_common_prefix(left: str, right: str) -> str:
    min_length = min(len(left), len(right))
    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]
    return left[:min_length]
