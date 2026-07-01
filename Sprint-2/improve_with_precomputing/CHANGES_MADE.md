# Changes Made: Optimization via Pre-computing

## Overview
These changes apply the strategy of **Pre-computing**: doing work upfront (like sorting or indexing) to make the primary search or calculation significantly faster. This allowed both algorithms to scale from small examples to datasets containing millions of items.

---

## 1. Longest Common Prefix Optimization (`common_prefix.py`)

### The Problem
The original implementation used a nested loop to compare every string in a list against every other string. 
- **Original Complexity**: $O(N^2)$.
- **The Bottleneck**: With 1,000,000 strings, the code would perform roughly 1 trillion comparisons, causing it to hang indefinitely.

### The Solution: "Sort Before Search"
I implemented alphabetical sorting as a pre-computation step. 
- **Why it works**: In a sorted list, the strings that share the longest common prefixes are mathematically guaranteed to be **neighbors**. 
- **The Change**: By sorting the list first, I replaced the nested loop with a single pass that only compares each string to the one immediately following it.
- **Improved Complexity**: $O(N \log N)$ for the sort + $O(N)$ for the single-pass search.
- **Legacy Retention**: Kept the original `find_common_prefix` helper function and variable names (`longest`, `string`, `other_string`) to maintain code continuity.

---

## 2. Count Letters Optimization (`count_letters.py`)

### The Problem
The original code contained a "hidden loop" inside a string iteration.
- **Original Complexity**: $O(N^2)$.
- **The Bottleneck**: The check `if letter.lower() not in s` required the computer to scan the entire string `s` for every character. On a 10-million-character string, this resulted in an impossible amount of work.

### The Solution: "Sets for Instant Lookups"
I introduced a pre-computed **Set** to handle character lookups.
- **Why it works**: Searching for an item in a Python `set` (a hash table) takes **O(1) constant time**, whereas searching a `string` takes **O(N) linear time**.
- **The Change**: I converted the string `s` into a set (`chars_in_string`) at the start of the function. This one-time $O(N)$ operation transformed the inner search from a slow scan into an instant lookup.
- **Improved Complexity**: $O(N)$ — one pass to build the set, and one pass to loop through the string.
- **Legacy Retention**: Preserved the original loop structure (`for letter in s`), the `is_upper_case` helper, and the `only_upper` variable name.

---

## 3. Technical Trade-offs: Space vs. Time
Both tasks are classic examples of the **Space-vs-Time trade-off**:

1.  **Memory (Space)**: We used extra memory to store a sorted version of the list (Task 5) and a set of unique characters (Task 6).
2.  **Speed (Time)**: By "spending" this memory, we drastically reduced the number of CPU operations required. 

**Result**: Operations that previously would have taken hours now complete in milliseconds, representing a massive gain in software scalability and performance.