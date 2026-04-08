"""
calculator.py
- Defines functions used to create a simple calculator
"""
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

######## Partner 1
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
##########################

def logarithm(n, base):
    if n <= 0:
        raise ValueError("Logarithm argument must be greater than 0")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(n, base)

######## Partner 1
def hypotenuse(a, b):
    # Returns the square root of (a^2 + b^2)
    return math.sqrt(a**2 + b**2)

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)
##########################





