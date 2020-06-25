import unittest

from aed_ds.queues.array_queue import ArrayQueue
from .test_queue import TestQueue
<<<<<<< HEAD
@unittest.SkipTest
=======


>>>>>>> 5bac28723bc0a9b0af35a408f9adfdcfbf3565c6
class TestArrayQueue(unittest.TestCase, TestQueue):
    def build_queue(self):
        self.queue = ArrayQueue(self.limit)

    def setUp(self):
        self.limit = 10
        self.build_queue()
<<<<<<< HEAD
<<<<<<< HEAD
        
if __name__ == "__main__":
    unittest.main()
=======

>>>>>>> 7841763ccee322ca4847cea594c761d35fee0866
=======
>>>>>>> 5bac28723bc0a9b0af35a408f9adfdcfbf3565c6
