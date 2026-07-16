def count_letters(s: str) -> int:

    lowers = set(ch for ch in s if ch.islower())
    uppers = set(ch for ch in s if ch.isupper())
    count = 0
    for ch in uppers:
        if ch.lower() not in lowers:
            count += 1
    return count
