import unittest
from assertions.calculator import calc


class CalculatorTest(unittest.TestCase):
    def test_sum_5_and_5_should_return_10(self):
        self.assertEqual(calc(5, 5), 10.0)


unittest.main()