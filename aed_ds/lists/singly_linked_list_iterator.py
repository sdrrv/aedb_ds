from .tad_iterator import Iterator
from ..exceptions import NoSuchElementException  

class SinglyLinkedListIterator(Iterator):
    def __init__(self, singly_linked_list):
        self.singly_linked_list = singly_linked_list
        self.position = self.singly_linked_list.get_head()

    # Returns true iff the iteration has more elements.
    # In other words, returns true next would return an element rather than throwing an exception.
    def has_next(self): 
        return (self.position != None)

    # Returns the next element in the iteration.
    # Throws NoSuchElementException
    def next(self): 
        if self.has_next():
            element = self.position.get_element()
            self.position = self.position.get_next()
            return element
        else:
            raise NoSuchElementException()

    # Restarts the iteration. After rewind, if the iteration is not empty, next will return the first element in the iteration.
    def rewind(self): 
        self.position = self.singly_linked_list.get_head()