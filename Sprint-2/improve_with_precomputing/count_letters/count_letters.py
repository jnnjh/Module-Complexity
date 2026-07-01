def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    only_upper = set()
    lowercase_letters = {letter for letter in s if not is_upper_case(letter)}
    for letter in s:
        if letter.lower() not in lowercase_letters:
            only_upper.add(letter)
    return len(only_upper)


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
