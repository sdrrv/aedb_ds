import unittest

from .test_stack import TestStack
from aed_ds.stacks.array_stack import ArrayStack


@unittest.SkipTest
class TestArrayStack(TestStack, unittest.TestCase):
    def build_stack(self):
        self.stack = ArrayStack(self.limit)

    def setUp(self):
        self.set_limit(10)
<<<<<<< HEAD
<<<<<<< HEAD
        
if __name__ == "__main__":
    unittest.main()
=======
>>>>>>> 7841763ccee322ca4847cea594c761d35fee0866
=======
>>>>>>> 5bac28723bc0a9b0af35a408f9adfdcfbf3565c6
