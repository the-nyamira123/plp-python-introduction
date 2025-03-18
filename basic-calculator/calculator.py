#!/usr/bin/python3
"""
Calculator Module
"""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers, handling division by zero."""
    return a / b if b != 0 else "Error: Division by zero."

def calculator(num1, num2, operation):
    """Perform a calculation based on the given operation."""
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    
    if operation in operations:
        return "{} {} {} = {}".format(num1, operation, num2, operations[operation](num1, num2))
    else:
        return "Invalid operation."

if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    print(calculator(num1, num2, operation))

