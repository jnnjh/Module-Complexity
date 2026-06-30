class Node:
    """
    A node in a double linked list.

    Each node supports a data, previous, and next
    - data: the value
    - previous: pointer to the previous node
    - next: pointer to the next node
    """

    _slots_ = ("data", "previous", "next")

    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class LinkedList:
    """
    Doubly Linked List

    Supports O(1) operations on insertion at head, removal from tail, and removal from arbitrary node
    """
    def __init__(self):
        # Head points to the first node in the list
        self.head = None
        
        # Tail points to the last node in the list
        self.tail = None

    def is_empty(self):
        """Returns True if the list contains no nodes."""
        return self.head is None

    def push_head(self, data):
        """
        Insert a new node at the head of the list.

        Time Complexity: O(1)

        Returns:
            Node: reference to the inserted node (handle for later removal)
        """
        node = Node(data)

        if self.is_empty():
            # If list is empty, head and tail both point to new node
            self.head = node
            self.tail = node
        else:
            # Link new node before current head
            node.next = self.head
            self.head.previous = node

            # Update head pointer
            self.head = node

        return node

    def pop_tail(self):
        """
        Remove and return the value at the tail of the list.

        Time Complexity: O(1)

        Raises:
            ValueError: if the list is empty
        """

        if self.is_empty():
            raise ValueError("List is empty.")
        
        # store value before removing node
        node = self.tail
        value = node.data

        self.remove(node)

        return value

    def remove(self, node):
        """
        Remove a node from the list using its reference.

        Time Complexity: O(1)

        Args:
            node (Node): the node to remove
        """
        if node.previous:
            node.previous.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

        node.previous = None
        node.next = None
    
    def move_to_head(self, node):
        """
        Move an existing node to the head of the list

        Time complexity: O(1)
        """

        if node is self.head:
            return
        
        self.remove(node)

        if self.is_empty():
            self.head = None
            self.tail = None
        else:
            node.previous = None
            node.next = self.head
            self.head.previous = node
            self.head = node

class LruCache:
    """
    Least Recently Used (LRU) Cache.

    Uses:
    - dictionary for O(1) lookup
    - doubly linked list for O(1) ordering

    Head = most recently used.
    Tail = least recently used.
    """
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("limit must be positive")

        self.limit = limit
        self.cache = {}
        self.list = LinkedList()

    def get(self, key):
        """
        Return value associated with key.

        Access counts as use.
        """
        node = self.cache.get(key)

        if node is None:
            return None

        self.list.move_to_head(node)

        return node.data[1]

    def set(self, key, value):
        """
        Insert or update a key.

        Update counts as use.
        """

        node = self.cache.get(key)

        # Existing key
        if node is not None:
            node.data = (key, value)
            self.list.move_to_head(node)
            return

        # Evict least recently used if full
        if len(self.cache) >= self.limit:
            evicted_key, _ = self.list.pop_tail()
            del self.cache[evicted_key]

        # Insert new entry
        node = self.list.push_head((key, value))
        self.cache[key] = node

    def __contains__(self, key):
        return key in self.cache

    def __len__(self):
        return len(self.cache)
