from typing import Dict

# 1. Create a dictionary to hold answers (the cache)
memo: Dict[int, int] = {}

def fibonacci(term_index: int) -> int:
    """
    Calculate the term_indexth Fibonacci number using memoisation.
    
    Time Complexity: O(n) - Each number up to n is calculated only once.
    Space Complexity: O(n) - To store the recursion stack and the memo dictionary.
    """
    # 2. The "Check": Do we already have the answer for term_index?
    if term_index in memo:
        return memo[term_index]

    # 3. Base cases
    if term_index <= 1:
        return term_index

    # 4. The "Store": Calculate and save the answer in the dictionary
    memo[term_index] = fibonacci(term_index - 1) + fibonacci(term_index - 2)
    
    # 5. Return the newly saved answer
    return memo[term_index]