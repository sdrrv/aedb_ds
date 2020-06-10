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
            return self.get_first()
        elif position == self.size()-1:
            return self.get_last()
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
            self.head.set_next(node)
            self.tail.set_previous(self.head)
        else:
            node.set_previous(self.tail)
            self.tail.set_next(node)
            self.tail = node
        self.count += 1

    def insert(self, element, position):
        if 0 > position or position > self.size():
            raise InvalidPositionException()
        else:
            if position == 0:
                self.insert_first(element)
            elif position == self.size():
                self.insert_last(element)
            else:
                node = self.head
                for _ in range(position-1):
                    node = node.get_next()
                new = DoubleListNode(element, node.get_next(), node)
                node.set_next(new)
                node.get_next().set_previous(new)
            self.count += 1

    def remove_first(self):
        if self.size() == 0:
            raise EmptyListException()
        else:
            if self.size() == 1:
                element = self.head.get_element()
                self.head = None
                self.tail = None
            else:
                element = self.head.get_element()
                self.head = self.head.get_next()
                self.head.set_previous(None)
            self.count -= 1
            return element

    def remove_last(self):
        if self.size() == 0:
            raise EmptyListException()
        else:
            if self.size() == 1:
                element = self.tail.get_element()
                self.head = None
                self.tail = None
            else:
                element = self.tail.get_element()
                tail = self.tail
                self.tail = self.tail.get_previous()
            self.count -= 1
            return element

    def remove(self, position):
        if position not in range(self.size()):
            raise InvalidPositionException()
        else:
            if position == 0:
                return self.remove_first()
            elif position == self.size()-1:
                return self.remove_last()
            else:
                node = self.head
                for _ in range(position):
                    node = node.get_next()
                node.get_previous().set_next(node.get_next())
                node.get_next().set_previous(node.get_previous())
                self.count -= 1
                return node.get_element()

    def iterator(self):
        return DoublyLinkedListIterator(self)
