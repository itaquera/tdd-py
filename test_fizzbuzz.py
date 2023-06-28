import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.fb = FizzBuzz()

if __name__ == '__main__':
    unittest.main()