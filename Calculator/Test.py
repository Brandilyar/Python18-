import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        args = 2,2,4
        self.calculator = Calculator(*args)

    def test_summa(self):
        self.assertEqual(self.calculator.summa(), 8)
    def test_difference(self):
        self.assertEqual(self.calculator.difference(), -4)
    def test_composition(self):
        self.assertEqual(self.calculator.composition(), 16)
    def test_division(self):
        self.assertEqual(self.calculator.division(), 0.25)


unittest.main()