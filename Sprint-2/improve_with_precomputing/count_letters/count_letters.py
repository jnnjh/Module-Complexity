def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    # we use two setts that contain unique letters in the string to scan only once
    uppers = set()
    lowers = set()
  
    for letter in s:
        if letter.islower():
            lowers.add(letter)
        elif letter.isupper():
            uppers.add(letter)
 
    only_upper_count = 0
    for upper_letter in uppers:
        if upper_letter.lower() not in lowers:
            only_upper_count += 1
            
    return only_upper_count


