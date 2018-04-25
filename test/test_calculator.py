import unittest
from dk.topdanmark.pythonsampleapplication.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Setup the test class"""
        self.calculator = Calculator()
        self.a = 10
        self.b = 5
        self.addition_result = 15
        self.subtraction_result = 5
        self.multiplication_result = 50
        self.division_result = 2
        self.floor_result = 8

    def test_addition(self):
        """Test for adding two numbers correctly correctly"""
        self.assertEqual(self.addition_result, self.calculator.addition(self.a, self.b))

    def test_subtraction(self):
        """Test for subtracting two numbers correctly correctly"""
        self.assertEqual(self.subtraction_result, self.calculator.subtraction(self.a, self.b))

    def test_multiplication(self):
        """Test for multiplying two numbers correctly correctly"""
        self.assertEqual(self.multiplication_result, self.calculator.multiplication(self.a, self.b))

    def test_division(self):
        """Test for dividing two numbers correctly correctly"""
        self.assertEqual(self.division_result, self.calculator.division(self.a, self.b))

    def test_floor_ir(self):
        """Test for floor'ing two numbers correctly correctly"""
        self.assertEqual(self.floor_result, self.calculator.floor_it(8.5))