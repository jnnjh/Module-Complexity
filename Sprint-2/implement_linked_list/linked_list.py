class Node:
    __slots__ = ("value", "next", "previous")

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

        return node

    def pop_tail(self):
        if self.tail is None:
            return None

        node = self.tail
        value = node.value

        self.remove(node)

        return value

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

        node.previous = None
        node.next = self.head

        if self.head is not None:
            self.head.previous = node

        self.head = node

        if self.tail is None:
            self.tail = node