class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, node):
        node.previous = None
        node.next = self.head

        if self.head is not None:
            self.head.previous = node

        self.head = node

        if self.tail is None:
            self.tail = node

    def remove(self, node):
        if node.previous is not None:
            node.previous.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

        node.next = None
        node.previous = None

    def move_to_head(self, node):
        if node == self.head:
            return

        self.remove(node)
        self.add_to_head(node)

    def remove_tail(self):
        if self.tail is None:
            return None

        node = self.tail
        self.remove(node)

        return node


class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be greater than 0")

        self.limit = limit
        self.cache = {}
        self.items = DoublyLinkedList()

    def get(self, key):
        node = self.cache.get(key)

        if node is None:
            return None

        self.items.move_to_head(node)

        return node.value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.items.move_to_head(node)
            return

        node = Node(key, value)

        self.cache[key] = node
        self.items.add_to_head(node)

        if len(self.cache) > self.limit:
            old_node = self.items.remove_tail()

            if old_node is not None:
                del self.cache[old_node.key]
