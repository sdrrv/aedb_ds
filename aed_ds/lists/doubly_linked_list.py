from .nodes import DoubleListNode
from ..exceptions import EmptyListException, InvalidPositionException
from .doubly_linked_list_iterator import DoublyLinkedListIterator
from .singly_linked_list import SinglyLinkedList


class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def get(self, position):
        pass

    def insert_first(self, element):
        pass

    def insert_last(self, element):
        pass

    def insert(self, element, position):
        pass

    def remove_first(self):
        pass

    def remove_last(self):
        pass

    def remove(self, position):
        pass

    def iterator(self):
        pass
