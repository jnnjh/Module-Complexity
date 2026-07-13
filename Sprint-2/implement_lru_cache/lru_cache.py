import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../implement_linked_list")))

from linked_list import LinkedList, Node # type:ignore
from typing import Any

class LruCache:
    def __init__(self, limit: int):
        if limit <= 0:
            raise ValueError("Limit must be greater than 0")
        self.capacity = limit
        # maps key
        self.cache: dict[Any, Node] = {} 
        # tracking the usage order head first tail last.
        self.list = LinkedList() 

    def get(self, key: Any) -> Any:
        # If key not exist return None
        if key not in self.cache:
            return None
            
        node_handle = self.cache[key]
        
        # we get  the value to return
        _, value = node_handle.value
        
        # we use remove() and push_head() to remove it from the position to the head
        self.list.remove(node_handle)
        self.cache[key] = self.list.push_head((key, value))
        
        return value

    def set(self, key: Any, value: Any) -> None:
        if key in self.cache:
            self.list.remove(self.cache[key])
            # we do this because the position and value about to change.
            del self.cache[key]
            
          # we call pop_tail() to cut off the tail
        elif len(self.cache) >= self.capacity:
            # return the value stored in the tail node
            oldest_item = self.list.pop_tail()
            if oldest_item:
                oldest_key, _ = oldest_item
                del self.cache[oldest_key]

        ## place the new items at the head of stack and update and return the object Node.
        new_node = self.list.push_head((key, value))
        self.cache[key] = new_node
