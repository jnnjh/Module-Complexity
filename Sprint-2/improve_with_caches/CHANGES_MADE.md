# Changes Made: Optimization via Memoisation

## Overview
The goal of these changes was to improve the performance of recursive functions that were previously performing redundant calculations. By introducing a manual cache (memoisation), the time complexity was reduced from exponential to linear.

## 1. Fibonacci Optimization (`fibonacci.py`)
- **Implemented Memoisation**: Introduced a dictionary named `memo` to store the results of each Fibonacci term as it is calculated.
- **Improved Complexity**: 
    - **Before**: $O(2^n)$ (Exponential) - The function recalculated the same branches of the recursion tree millions of times.
    - **After**: $O(n)$ (Linear) - Each term is calculated exactly once and then retrieved from the cache.
- **Readability**: Renamed the parameter `n` to `term_index` to more clearly describe that the function is looking for a specific position in a sequence.

## 2. Making Change Optimization (`making_change.py`)
- **Recursive Helper Pattern**: Refactored the original iterative-recursive logic into a dedicated helper function (`ways_to_make_change_helper`) to better support memoisation.
- **State Tracking**: 
    - Created a **state key** using a Tuple: `(total, len(coins))`. 
    - **The "Why"**: A unique solution depends on both the amount of money left and which coins are still available. A tuple is used because it is immutable and can be used as a dictionary key.
- **Logic Refinement**: 
    - Updated the base case to return `1` when `total == 0`, representing a successful combination.
    - Added `memo.clear()` in the wrapper function to ensure the cache is fresh for every new call to the main function.
- **Legacy Preservation**: Maintained original variable names (`coin`, `count_of_coin`, `intermediate`) while implementing the performance improvements.

## 3. Technical Trade-offs: Space vs. Time
In both implementations, I applied the **Space-vs-Time trade-off**:
- **The Cost (Space)**: Increased memory usage to store the `memo` dictionary.
- **The Benefit (Time)**: Drastic reduction in execution time. For example, `ways_to_make_change(9176)` now returns a result instantly, whereas the unoptimised version would likely never finish on standard hardware.