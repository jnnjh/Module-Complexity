class Node:
    """
    Step 1: Updated Node class.
    Each node stores both key and value so we can find the 
    dictionary entry when a node is evicted from the tail.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    """
    A Doubly Linked List to track the order of usage.
    Head is Most Recently Used (MRU).
    Tail is Least Recently Used (LRU).
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, node):
        """Adds an existing node to the front of the list."""
        node.next = self.head
        node.previous = None
        
        if self.head is not None:
            self.head.previous = node
        
        self.head = node
        
        # If list was empty, this node is also the tail
        if self.tail is None:
            self.tail = node

    def pop_tail(self):
        """Removes the last node (the oldest item) and returns it."""
        if self.tail is None:
            return None

        old_tail = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            
        return old_tail

    def remove(self, node):
        """Unplucks a node from its current position in the list."""
        if node.previous is not None:
            node.previous.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous
            
        # Clean up pointers of the removed node
        node.next = None
        node.previous = None


class LruCache:
    """
    The LRU Cache: Dictionary + Linked List.
    Provides O(1) time complexity for both get and set operations.
    """
    def __init__(self, limit):
        # 1. Validation
        if limit < 1:
            raise ValueError("Cache limit must be at least 1.")
            
        # 2. Store the limit
        self.limit = limit
        
        # 3. Dictionary for O(1) key lookups (Key -> Node)
        self.lookup = {}
        
        # 4. Doubly Linked List for O(1) ordering
        self.order = LinkedList()

    def get(self, key):
        """
        Logic for get(key):
        Find the item, move it to the front, return value.
        """
        if key not in self.lookup:
            return None
            
        node = self.lookup[key]
        
        # Move to front (Most Recently Used)
        self.order.remove(node)
        self.order.push_head(node)
        
        return node.value

    def set(self, key, value):
        """
        Logic for set(key, value):
        If exists: update and move to front.
        If new: check limit, evict tail if full, then add to front.
        """
        if key in self.lookup:
            # Update existing
            node = self.lookup[key]
            node.value = value
            self.order.remove(node)
            self.order.push_head(node)
        else:
            # Check limit
            if len(self.lookup) >= self.limit:
                # Evict the oldest (tail)
                evicted_node = self.order.pop_tail()
                if evicted_node:
                    del self.lookup[evicted_node.key]
            
            # Create and add new node
            new_node = Node(key, value)
            self.order.push_head(new_node)
            self.lookup[key] = new_node