# Changes Made: LRU Cache Implementation

## 1. Architectural Overview
To achieve the requirement of **O(1) time complexity** for both `get` and `set` operations, I implemented a hybrid data structure combining a **Python Dictionary** and a **Doubly Linked List**.

- **The Dictionary (`self.lookup`)**: Provides constant time O(1) access to any node using its key.
- **The Doubly Linked List (`self.order`)**: Maintains the "recency" of items. The **Head** represents the Most Recently Used (MRU) item, and the **Tail** represents the Least Recently Used (LRU) item.

## 2. Component Breakdown

### Node Class
- **Key-Value Storage**: Unlike a standard linked list node, these nodes store both the `key` and the `value`. 
- **The "Why"**: Storing the `key` is essential during eviction. When we remove the tail node from the list, we must also delete its corresponding entry from the dictionary. The node must "know" its key so we can perform this reverse lookup.

### LinkedList Class
- **Pointer Management**: Manages `head` and `tail` pointers.
- **Methods**:
    - `push_head(node)`: Places a node at the front (MRU position).
    - `pop_tail()`: Removes the oldest node (LRU position) and returns the node object so the Cache can identify which key to delete.
    - `remove(node)`: Disconnects a node from its current position. This is used when an existing item is accessed or updated and needs to be moved to the front.

### LruCache Class
- **`get(key)`**: 
    1. Checks the dictionary for the key.
    2. If found, it uses `remove()` and `push_head()` to move the node to the front of the list, marking it as recently used.
- **`set(key, value)`**:
    1. **If key exists**: Updates the value and moves the node to the front.
    2. **If key is new**: 
        - Checks if the cache is at its `limit`.
        - If full, it calls `pop_tail()` and deletes that node's key from the dictionary.
        - Adds the new node to both the dictionary and the front of the list.

## 3. Complexity & Trade-offs
- **Time Complexity**: Every operation (`get` and `set`) is **O(1)** because dictionary lookups and linked list pointer updates do not depend on the size of the cache.
- **Space Complexity**: I traded **Space for Time**. I used extra memory to store:
    1. A dictionary entry for every item.
    2. Two pointers (`next` and `previous`) for every node.
- **Trade-off Choice**: This extra memory usage is worth the benefit of having a cache that never slows down, even as the limit increases to thousands of items.

## 4. Testing Suite
I expanded the test suite to include several critical edge cases:
- **Update Existing Key**: Verified that re-setting a key updates the value and refreshes its "recency" status.
- **Limit of One**: Confirmed that a cache with a limit of 1 correctly evicts the old item every time a new one is added.
- **Non-existent Keys**: Ensured that the cache gracefully returns `None` for missing keys.
- **Complex Values**: Verified that the cache can store non-primitive types like lists, proving it stores data by reference.