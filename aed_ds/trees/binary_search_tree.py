from .tad_tree import Tree
from ..dictionaries.tad_ordered_dictionary import OrderedDictionary
from ..exceptions import DuplicatedKeyException, NoSuchElementException, \
    EmptyDictionaryException
from .nodes.binary_nodes import BinarySearchTreeNode


class BinarySearchTree(OrderedDictionary, Tree):
    def __init__(self,max_size):
        self.max_size = max_size  #just because
        self.count = 0
        self.height_value = None
        self.root = None
        
    # Returns the number of elements in the dictionary.
    def size(self):
            return self.count

    # Returns true if the dictionary is full.
    def is_full(self):
        if self.count<self.max_size:
            return False
        return True

    # Returns the value associated with key k.
    # Throws NoSuchElementException
    def get(self, k):
        result = self.recursive_get(self.get_root,k)
        if not result:
            raise NoSuchElementException()
        return result.get_element()

    def recursive_get(self,current_node,k):
        if current_node:
            current_key = current_node.get_key()
            if current_key==k:
                return current_node
            elif k < current_key:
                self.recursive_get(current_node.get_left_child())
            elif k > current_key:
                self.recursive_get(current_node.get_right_child())


    # Inserts a new value, associated with key k.
    # Throws DuplicatedKeyException
    def insert(self, k, v): pass

    # Updates the value associated with key k.
    # Throws NoSuchElementException
    def update(self, k, v): pass

    # Removes the key k, and the value associated with it.
    # Throws NoSuchElementException
    def remove(self, k):
        
        pass

    # Returns a List with all the keys in the dictionary.
    def keys(self): pass

    # Returns a List with all the values in the dictionary.
    def values(self): pass

    # Returns a List with all the key value pairs in the dictionary.
    def items(self): pass

    # Returns an iterator of the elements in the dictionary
    def iterator(self): pass

    # Returns the element with the smallest key
    # Throws EmptyTreeException
    def get_min_element(self): pass
    
    # Returns the element with the largest key
    # Throws EmptyTreeException
    def get_max_element(self): pass

    # Returns the root of the tree
    # Throws EmptyTreeException
    def get_root(self):
        return self.root

    # Returns the height of the tree
    # Throws EmptyTreeException
    def height(self):
        if not self.height_value:
            self.remake_height()
        return self.height_value
        

    # Returns True if the tree is empty
    def is_empty(self):
        if self.count == 0:
            return True
        return False
    
    #Remakes the height 
    def remake_height(self):pass