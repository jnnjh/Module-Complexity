import random

MAX_LEVEL = 4


class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * level


class SkipList:
    def __init__(self):
        self.head = Node(None, MAX_LEVEL)
        self.level = 1

    def _random_level(self):
        level = 1

        while level < MAX_LEVEL and random.random() < 0.5:
            level += 1

        return level

    def insert(self, value):
        update = [None] * MAX_LEVEL
        current = self.head

        for i in range(self.level - 1, -1, -1):
            while (
                current.forward[i] is not None
                and current.forward[i].value < value
            ):
                current = current.forward[i]

            update[i] = current

        node_level = self._random_level()

        if node_level > self.level:
            for i in range(self.level, node_level):
                update[i] = self.head

            self.level = node_level

        new_node = Node(value, node_level)

        for i in range(node_level):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def __contains__(self, value):
        current = self.head

        for i in range(self.level - 1, -1, -1):
            while (
                current.forward[i] is not None
                and current.forward[i].value < value
            ):
                current = current.forward[i]

        current = current.forward[0]

        return current is not None and current.value == value

    def to_list(self):
        result = []
        current = self.head.forward[0]

        while current is not None:
            result.append(current.value)
            current = current.forward[0]

        return result