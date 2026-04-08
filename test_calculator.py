import math

class TestCalculator(unittest.TestCase):

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(-12, 4), -3)
    ##########################

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(8, 15), 17.0)

    def test_sqrt(self): # 3 assertions
        # Test
        self.assertEqual(square_root(16), 4.0)
        self.assertEqual(square_root(25), 5.0)
        # Test for invalid argument
        with self.assertRaises(ValueError):
            square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()