import unittest

from linked_list import LinkedList

class LinkedListTest(unittest.TestCase):
    def test_pushes_then_pops(self):
        l = LinkedList()
        l.push_head("a")
        l.push_head("b")
        l.push_head("c")

        self.assertEqual(l.pop_tail(), "a")
        self.assertEqual(l.pop_tail(), "b")
        self.assertEqual(l.pop_tail(), "c")

    def test_remove(self):
        l = LinkedList()
        l.push_head("a")
        b = l.push_head("b")
        l.push_head("c")

        l.remove(b)

        self.assertEqual(l.pop_tail(), "a")
        self.assertEqual(l.pop_tail(), "c")

    def test_remove_tail(self):
        l = LinkedList()
        a = l.push_head("a")
        b = l.push_head("b")
        l.remove(a)
        self.assertEqual(l.head, b)
        self.assertEqual(l.tail, b)
        self.assertIsNone(b.next)
        self.assertIsNone(b.previous)

    def test_remove_middle(self):
        l = LinkedList()
        l.push_head("tail_node")  
        middle = l.push_head("middle_node")
        l.push_head("head_node") 

        l.remove(middle)

        self.assertEqual(l.head.value, "head_node")
        self.assertEqual(l.tail.value, "tail_node")
        self.assertEqual(l.head.next.value, "tail_node")
        self.assertEqual(l.tail.previous.value, "head_node")

    def test_pop_empty_list(self):
        l = LinkedList()
        # If the list is empty, popping the tail should return None 
        # instead of crashing the program with an error.
        result = l.pop_tail()

        self.assertIsNone(result)

    def test_remove_none(self):
        l = LinkedList()
        l.push_head("a")
        # This should just do nothing and not crash
        l.remove(None)
        
        self.assertEqual(l.pop_tail(), "a")

if __name__ == "__main__":
    unittest.main()
