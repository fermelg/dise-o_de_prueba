import unittest
from src.calculator import add, divide, mean

class TestCalculatorUnit(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertAlmostEqual(add(2.5, 0.5), 3.0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_mean(self):
        self.assertEqual(mean([2, 4, 6]), 4)
        self.assertIsNone(mean([]))

if __name__ == "__main__":
    unittest.main()