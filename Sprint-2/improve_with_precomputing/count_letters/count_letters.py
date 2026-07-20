def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    lowercase_letters = {letter for letter in s if letter.islower()}

    only_upper = set()

    for letter in s:
        if letter.isupper() and letter.lower() not in lowercase_letters:
            only_upper.add(letter)

    return len(only_upper)