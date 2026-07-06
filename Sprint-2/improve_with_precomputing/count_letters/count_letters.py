def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    letters_in_string = set(s)

    only_upper = set()

    for letter in s:
        if is_upper_case(letter):
            if letter.lower() not in letters_in_string:
                only_upper.add(letter)

    return len(only_upper)


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()