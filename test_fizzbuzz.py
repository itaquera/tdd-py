import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.fb = FizzBuzz()

    def test_numero_divisivel_por_tres(self):
        self.assertEqual(self.fb.fizz(3), "Fizz")

    def test_numero_divisivel_por_cinco(self):
        self.assertEqual(self.fb.buzz(5), "Buzz")

    def test_numero_divisivel_por_tres_e_cinco(self):
        self.assertEqual(self.fb.fizzbuzz(15), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()