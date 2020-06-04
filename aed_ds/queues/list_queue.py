from .tad_queue import Queue
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import EmptyQueueException, FullQueueException


class ListQueue(Queue):
    def __init__(self):
        self.list = SinglyLinkedList()

    def is_empty(self):
        return self.list.size() == 0

    def is_full(self):
        return False

    def size(self):
        return self.list.size()

    def enqueue(self, element):
        if self.is_full():
            raise FullQueueException()
        else:
            return self.list.size()

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueException()
        else:
            self.list.remove_first()

