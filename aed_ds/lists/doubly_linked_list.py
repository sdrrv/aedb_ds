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
        if self.size() == 0:
            raise EmptyListException()
        elif position == 0:
            return get_first()
        elif position == self.size()-1:
            return get_last()
        else:
            node = self.head
            for _ in range(position):
                node = node.get_next()
            return node.get_element()

    def insert_first(self, element):
        node = DoubleListNode(element, None, None)
        if self.size() == 0:
            self.head = node
            self.tail = node
        elif self.size() == 1:
            self.head = node
            self.head.set_next(self.tail)
            self.tail.set_previous(self.head)
        else:
            node.set_next(self.head)
            self.head.set_previous(node)
            self.head = node
        self.count += 1

    def insert_last(self, element):
        node = DoubleListNode(element, None, None)
        if self.size() == 0:
            self.head = node
            self.tail = node
        elif self.size() == 1:
            self.tail = node
            self.head.set_next(self.tail)
            self.tail.set_previous(self.head)
        else:
            node.set_previous(self.tail)
            self.tail.set_next(node)
            self.tail = node
        self.count += 1

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
