#!/usr/bin/python3
"""
Test file for Calculator Module
"""

from calculator import add, subtract, multiply, divide, calculator

def print_result(result):
    """Print the result of a calculation."""
    print(result)

if __name__ == "__main__":
    print_result(calculator(10, 5, '+'))  # Expected output: "10 + 5 = 15"
    print_result(calculator(10, 5, '-'))  # Expected output: "10 - 5 = 5"
    print_result(calculator(10, 5, '*'))  # Expected output: "10 * 5 = 50"
    print_result(calculator(10, 5, '/'))  # Expected output: "10 / 5 = 2.0"
    print_result(calculator(10, 0, '/'))  # Expected output: "Error: Division by zero."

    # Testing individual arithmetic functions
    print_result(add(10, 5))       # Expected output: 15
    print_result(subtract(10, 5))  # Expected output: 5
    print_result(multiply(10, 5))  # Expected output: 50
    print_result(divide(10, 5))    # Expected output: 2.0
    print_result(divide(10, 0))    # Expected output: "Error: Division by zero."

