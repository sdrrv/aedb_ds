from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList
from .item import Item 

import ctypes 

class HashTable(Dictionary):
    def __init__(self, size=101):
        self.array_size = size
        self.num_elements = 0
        self.table = (self.array_size * ctypes.py_object)() # Array of pointers

        # Create an empty list for each table position
        for i in range(self.array_size):
            self.table[i] = SinglyLinkedList()

    def size(self):
        return self.num_elements

    def is_full(self):
        return self.num_elements == self.array_size

    def get(self, k):
        if not has_key():
            raise NoSuchElementException()
        else:
            idx = self.table[self.hashfunction(k)]
            for _ in range(self.size()):
                node = idx.iterator().next()
                if node.get_element().get_key() == k:
                    return node.get_element().get_value()

    def insert(self, k, v):
        # Check if it has key
        if self.has_key(k):
            raise DuplicatedKeyException()

        ## Insert new item
        # Calculate the table index
        idx = self.hash_function(k) # O(1)
        # Create a new Item
        item = Item(k, v)
        # Insert the item in the colision list
        self.table[idx].insert_last(item)
        # Update the number of elements
        self.num_elements += 1    

    def update(self, k, v):
        if self.has_key(k):
            raise NoSuchElementException()
        idx= self.hash_function(k)
        it = self.table[idx].iterator()
        while it.has_next():
            node = it.next()
            if node.get_key()== k:
                node.set_value(v)
                return True

    def remove(self, k): pass

    def keys(self):
        result = SinglyLinkedList()
        for index in self.table:
            while index.iterator().has_next():
                result.insert_last(index.iterator().next().get_key())
        return result

    def values(self): pass

    def items(self): pass

    def hash_function(self, k):
        return sum([ord(c) for c in k]) % self.array_size

    def has_key(self, k):
        idx = self.hash_function(k) # O(1)    
        colision_list = self.table[idx]
        it = colision_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                return True
        return False