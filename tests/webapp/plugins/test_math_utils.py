import unittest
from webapp.plugins.math_utils import isPrimeNumber

class TestMathUtils(unittest.TestCase):

    def test_prime_number_true(self):
        result = isPrimeNumber(97)
        self.assertTrue(result[0])

    def test_prime_number_false(self):
        result = isPrimeNumber(111)
        self.assertFalse(result[0])
        self.assertEquals(37, result[1])

    def test_prime_number_zero(self):
        result = isPrimeNumber(0)
        self.assertTrue(result[0])

    def test_prime_number_one(self):
        result = isPrimeNumber(1)
        self.assertTrue(result[0])

    def test_prime_number_two(self):
        result = isPrimeNumber(2)
        self.assertTrue(result[0])
