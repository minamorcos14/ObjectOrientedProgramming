from MathOperations.addition import Addition;
from MathOperations.subtraction import Subtraction;

class Calculator:
    Result = 0
    def __init__(self):
        pass

    def addition(self, a, b):
        return float(a) + float(b)

    def subtraction(self, a, b):
        return float(a) - float(b)