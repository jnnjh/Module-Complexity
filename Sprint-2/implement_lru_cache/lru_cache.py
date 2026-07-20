from typing import Any, Optional


class Node:
    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value
        self.previous: Optional["Node"] = None
        self.next: Optional["Node"] = None


class LruCache:
    def __init__(self, limit: int):
        if limit <= 0:
            raise ValueError("Limit must be greater than zero")

        self.limit = limit
        self.cache = {}
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def _remove_node(self, node: Node):
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

    def _add_to_head(self, node: Node):
        node.previous = None
        node.next = self.head

        if self.head:
            self.head.previous = node
        else:
            self.tail = node

        self.head = node

    def get(self, key):
        node = self.cache.get(key)

        if node is None:
            return None

        self._remove_node(node)
        self._add_to_head(node)

        return node.value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_head(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_head(node)

        if len(self.cache) > self.limit:
            lru = self.tail
            self._remove_node(lru)
            del self.cache[lru.key]