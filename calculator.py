import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example
import math

def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm requires positive values.")
    return math.log(b, a)
def exp(a, b):
    return a ** b



#################### Partner 1 Functions Start ####################

def

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

#################### Partner 1 Functions End ####################