from .tad_stack import Stack
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import FullStackException,  EmptyStackException


class ListStack(Stack):
    def __init__(self):
        self.list = SinglyLinkedList()

    def is_empty(self):
        return self.list.size() == 0

    def is_full(self):
        return False

    def size(self):
        return self.list.size()

    def top(self):
        return self.list.get_last()

    def push(self, element):
        if self.is_full():
            raise FullStackException()
        else:
            self.list.insert_last(element)

    def pop(self):
        if self.is_empty():
            raise EmptyStackException()
        else:
            self.list.remove_last()

