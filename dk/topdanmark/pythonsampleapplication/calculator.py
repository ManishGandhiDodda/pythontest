import math

"""
Class Calculator

This class does some simple mathematic operations.
"""


class Calculator:
    """Class Calculator"""

    @staticmethod
    def addition(a, b):
        """
        addition

        Takes two numbers and adds them.
        """
        return a + b

    @staticmethod
    def subtraction(a, b):
        """
        subtraction

        Takes two numbers and subtracts the second from the first.
        """
        return a - b

    @staticmethod
    def multiplication(a, b):
        """
        multiplication

        Takes two numbers and multiplies them.
        """
        return a * b

    @staticmethod
    def division(a, b):
        """
        division

        Takes two numbers and divides the first by the first.
        """
        return a/b

    @staticmethod
    def floor_it(a):
        """
        floor_it

        Rounds the number down to the nearest integer.
        """

        return math.floor(a)
