class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.previous = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        return new_node
    
    def pop_tail(self):
        if self.tail is None:
            return None
        data = self.tail.data
        if self.tail.previous:
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            self.head = None
            self.tail = None
        return data

    def remove(self, node):
        if node.previous:
            node.previous.next = node.next
        else:
            self.head = node.next
        
        if node.next:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

