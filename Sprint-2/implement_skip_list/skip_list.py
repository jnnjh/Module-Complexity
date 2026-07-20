import random


MAX_LEVEL = 16
P = 0.5


class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)


class SkipList:
    def __init__(self):
        self.level = 0
        self.head = Node(None, MAX_LEVEL)

    def _random_level(self):
        level = 0
        while random.random() < P and level < MAX_LEVEL:
            level += 1
        return level

    def insert(self, value):
        update = [None] * (MAX_LEVEL + 1)
        current = self.head

        for i in range(self.level, -1, -1):
            while (
                current.forward[i] is not None
                and current.forward[i].value < value
            ):
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current is not None and current.value == value:
            return

        new_level = self._random_level()

        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.head
            self.level = new_level

        new_node = Node(value, new_level)

        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def __contains__(self, value):
        current = self.head

        for i in range(self.level, -1, -1):
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