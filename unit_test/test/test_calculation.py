import unittest
from src.calculation import  add, subtract, multiply, divide
class TestCalculation(unittest.TestCase):
    def test_add(self):
        res = add(10, 5)
        self.assertEqual(15,res, "Addition Error")
    def test_sub(self):
        res = subtract(10, 5)
        self.assertEqual(5,res, "Subtraction Error")
    def test_mul(self):
        res = multiply(10, 5)
        self.assertEqual(50,res, "Multiplication Error")
    def test_div(self):
        res = divide(10, 5)
        self.assertEqual(2.0,res, "Division Error")
