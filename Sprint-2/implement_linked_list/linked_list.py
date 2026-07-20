from typing import Any, Optional


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.previous: Optional["Node"] = None
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def push_head(self, value: Any) -> Node:
        node = Node(value)

        node.next = self.head

        if self.head is not None:
            self.head.previous = node
        else:
            self.tail = node

        self.head = node
        return node

    def pop_tail(self):
        if self.tail is None:
            return None

        node = self.tail

        if node.previous is not None:
            self.tail = node.previous
            self.tail.next = None
        else:
            self.head = None
            self.tail = None

        node.previous = None
        node.next = None

        return node.value

    def remove(self, node: Node) -> None:
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