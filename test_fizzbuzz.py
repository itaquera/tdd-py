import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.fb = FizzBuzz()

    def test_numero_divisivel_por_tres(self):
        self.assertEqual(self.fb.calculate(3), "Fizz")

    def test_numero_divisivel_por_cinco(self):
        self.assertEqual(self.fb.calculate(5), "Buzz")

    def test_numero_divisivel_por_tres_e_cinco(self):
        self.assertEqual(self.fb.calculate(15), "FizzBuzz")

    def test_numero_nao_divisivel_por_tres_e_cinco(self):
        self.assertEqual(self.fb.calculate(4), "4")

if __name__ == '__main__':
    unittest.main()