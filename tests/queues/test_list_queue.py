import unittest

from aed_ds.queues.list_queue import ListQueue
from .test_queue import TestQueue


@unittest.SkipTest
class TestListQueue(unittest.TestCase, TestQueue):
    def build_queue(self):
        self.queue = ListQueue()

    def setUp(self):
        self.build_queue()
<<<<<<< HEAD
        
if __name__ == "__main__":
    unittest.main()
=======

>>>>>>> 7841763ccee322ca4847cea594c761d35fee0866
