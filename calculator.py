import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def exp(a, b):
    return a ** b

def logarithm(n, base):
    if n <= 0:
        raise ValueError("Logarithm argument must be greater than 0")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(n, base)

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)






