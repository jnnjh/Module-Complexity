from typing import List

def find_longest_common_prefix(strings: List[str]):
    """
    Optimized version using pre-sorting while keeping legacy names and helpers.
    """
    # Edge case handling
    if len(strings) < 2:
        return ""

    # Pre-compute (Sort) - This is the optimization!
    strings.sort()

    longest = ""

    # Single loop replacing the nested loop
    for string_index in range(len(strings) - 1):
       
        string = strings[string_index]
        other_string = strings[string_index + 1]

        common = find_common_prefix(string, other_string)

        if len(common) > len(longest):
            longest = common
            
    return longest


def find_common_prefix(left: str, right: str) -> str:
    min_length = min(len(left), len(right))
    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]
    return left[:min_length]