import unittest
from impl import fibonacci

class TestFactorial(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(fibonacci(5), 8)

    def test_list(self):
        self.assertEqual([fibonacci(n) for n in range(6)], [1,1,2,3,5,8])

    def test_minus(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
