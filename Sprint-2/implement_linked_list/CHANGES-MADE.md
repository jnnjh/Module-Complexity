# Changes Made: Doubly Linked List Implementation

## 1. Core Logic (`linked_list.py`)
- **Node Class**: Created a `Node` class to act as the building block of the list. Each node stores a `value` and has pointers for `next` and `previous`, allowing for bi-directional traversal.
- **LinkedList Class**: 
    - Implemented `push_head(value)`: Adds a new node to the beginning of the list in **O(1)** time.
    - Implemented `pop_tail()`: Removes and returns the value from the end of the list in **O(1)** time. Includes logic for empty lists and single-node lists.
    - Implemented `remove(node)`: Removes a specific node from the list and re-wires the surrounding nodes' pointers. Handles edge cases where the node is the current `head` or `tail`.

## 2. Testing & Verification (`linked_list_test.py`)
- **Middle Removal**: Added `test_remove_middle` to verify that when a node in the center of the list is removed, the nodes ahead and behind it correctly link to each other.
- **Edge Case - Empty Pop**: Added `test_pop_empty_list` to ensure the program returns `None` rather than crashing when attempting to remove from an empty list.
- **Edge Case - Null Removal**: Added `test_remove_none` to verify the `remove` method handles `None` inputs gracefully.

## 3. Technical Trade-offs
- **Space vs. Time**: Used a Doubly Linked List structure, trading slightly more memory (for the `previous` pointer) to achieve faster removal and tail-access times **`O(1)`**.