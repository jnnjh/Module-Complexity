from typing import Optional


class _Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional["_Node"] = None
        self.prev: Optional["_Node"] = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        new_node = _Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next  = self.head
            self.head.prev = new_node
            self.head      = new_node

        return new_node

    def pop_tail(self):
        if self.tail is None:
            return None

        value = self.tail.value

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None

        return value

    def remove(self, node):
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

        elif node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None

        else:
            node.prev.next = node.next
            node.next.prev = node.prev
