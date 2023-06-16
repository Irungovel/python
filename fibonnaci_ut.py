import unittest

import fibonnaci
from fibonnaci import *

class TestFibonacciSequence(unittest.TestCase):

    def test_fibFor8(self):
        self.assertEquals(fibonnaci.fibObject.max_fibValue, 55)

if __name__ == '__main__':
    unittest.main()