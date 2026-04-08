import unittest
import math
from calculator import add, sub, mul, div, log, exp

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)

    def test_subtract(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(0, 7), -7)
        self.assertEqual(sub(-3, -3), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self):
        self.assertEqual(log(2, 8), 3.0)
        self.assertEqual(log(10, 100), 2.0)
        self.assertAlmostEqual(log(math.e, math.e), 1.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(-1, 10)
        with self.assertRaises(ValueError):
            log(1, 10)
        with self.assertRaises(ValueError):
            log(10, -5)

if __name__ == '__main__':
    unittest.main()