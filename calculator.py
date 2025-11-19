import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""


#################### Partner 1 Functions Start ####################

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

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Error: cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 1 or b <= 0:
        raise ValueError("Error: invalid domain for log function")
    return log(b, a)

def exp(a, b):
    a ** b

#################### Partner 1 Functions End ####################