class Node:
    __slots__ = ('value', 'next', 'previous')

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
            raise IndexError('pop from empty list')
        node = self.tail
        value = node.value
        if node.previous is None:
            self.head = None
            self.tail = None
        else:
            self.tail = node.previous
            self.tail.next = None
            node.previous = None
        node.next = None
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
