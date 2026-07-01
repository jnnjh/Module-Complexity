from typing import Optional

class _Node:
    
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev: Optional["_Node"] = None
        self.next: Optional["_Node"] = None
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: _Node):
        assert node.prev is not None
        assert node.next is not None
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_front(self, node: _Node):
        next_node = self.head.next
        assert next_node is not None
        node.next = next_node
        node.prev = self.head
        next_node.prev = node
        self.head.next = node

    def remove_last(self) -> _Node:
        lru = self.tail.prev
        assert lru is not None
        self.remove(lru)
        return lru


class LruCache:
    
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("limit must be positive")
        
        self.limit = limit
        self.cache = {}
        self.list = DoublyLinkedList()

    def get(self, key):
        if key not in self.cache:
            return None
        
        node = self.cache[key]
        self.list.remove(node)
        self.list.add_to_front(node)
        return node.value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.list.remove(node)
            self.list.add_to_front(node)
            return

        node = _Node(key, value)
        self.cache[key] = node
        self.list.add_to_front(node)

        if len(self.cache) > self.limit:
            lru = self.list.remove_last()
            del self.cache[lru.key]
