# https://github.com/jngabbard/lab11-JG-LP
# Partner 1: Joshua Gabbard
# Partner 2: Leslie Paulsen

import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm requires positive values.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

    return a / b


def square_root(a):
    if a < 0:
        raise ValueError("Error: cannot calculate the square root of a negative number")
    math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def log(a, b):
    if a <= 1 or b <= 0:
        raise ValueError("Error: invalid domain for log function")
    return log(b, a)

def exp(a, b):
    a ** b
