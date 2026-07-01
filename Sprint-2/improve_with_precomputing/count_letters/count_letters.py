def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    
    Optimized via Pre-computing: We convert the string to a set upfront to make 
    the 'not in' check a constant-time operation.
    """
    # PRE-COMPUTING: Create a set of all unique characters in the string.
    # Searching a set takes O(1) time, while searching a string takes O(N) time.
    chars_in_string = set(s)

    only_upper = set()
    # LEGACY LOOP: Iterate through the string as originally designed.
    for letter in s:
        if is_upper_case(letter):
            # OPTIMIZATION: Check against the pre-computed set instead of the full string 's'.
            if letter.lower() not in chars_in_string:
                only_upper.add(letter)
    return len(only_upper)


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()