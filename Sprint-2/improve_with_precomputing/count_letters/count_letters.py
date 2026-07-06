def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    # Precompute a set of all characters in s: O(n) once.
    # This turns the `letter.lower() not in s` check (O(n) linear scan,
    # making the whole function O(n^2)) into an O(1) set lookup,
    # bringing the overall complexity down to O(n).
    letters = set(s)
    only_upper = set()
    
    for letter in s:
        if letter.isupper():
            if letter.lower() not in letters:
                only_upper.add(letter)
    return len(only_upper)
