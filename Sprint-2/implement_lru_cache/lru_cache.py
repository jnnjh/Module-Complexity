class _Node:
    __slots__ = ('key', 'value', 'previous', 'next')

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError('limit must be greater than zero')
        self.limit = limit
        self.map = {}
        self.head = None
        self.tail = None
        self.size = 0

    def _unlink(self, node):
        if node.previous is not None:
            node.previous.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

        node.previous = None
        node.next = None

    def _link_head(self, node):
        node.previous = None
        node.next = self.head
        if self.head is not None:
            self.head.previous = node
        self.head = node
        if self.tail is None:
            self.tail = node

    def _move_to_head(self, node):
        if node is self.head:
            return
        self._unlink(node)
        self._link_head(node)

    def _evict_tail(self):
        if self.tail is None:
            return
        node = self.tail
        self._unlink(node)
        del self.map[node.key]
        self.size -= 1

    def set(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._move_to_head(node)
            return

        node = _Node(key, value)
        self.map[key] = node
        self._link_head(node)
        self.size += 1

        if self.size > self.limit:
            self._evict_tail()

    def get(self, key):
        node = self.map.get(key)
        if node is None:
            return None
        self._move_to_head(node)
        return node.value
