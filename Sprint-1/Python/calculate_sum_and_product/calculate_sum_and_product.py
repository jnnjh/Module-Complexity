from typing import Dict, List


def calculate_sum_and_product(input_numbers: List[int]) -> Dict[str, int]:
    """
    Calculate the sum and product of integers in a list.

    Note: the sum is every number added together
    and the product is every number multiplied together
    so for example: [2, 3, 5] would return
    {
        "sum": 10,
        "product": 30
    }

    Time Complexity: O(n)
    Space Complexity: O(1)
    Optimal Time Complexity: O(n)

    Analysis:
    - The original implementation loops through the list twice:
      once to calculate the sum and once to calculate the product.
    - Two separate linear loops are still O(n), since Big O ignores
      constant factors (2n simplifies to O(n)).
    - The implementation can be optimized by combining both calculations
      into a single loop, reducing the number of iterations.
    """

    # Edge case: empty list
    if not input_numbers:
        return {"sum": 0, "product": 1}

    total = 0
    product = 1

    for current_number in input_numbers:
        total += current_number
        product *= current_number

    return {"sum": total, "product": product}