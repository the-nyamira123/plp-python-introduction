#!/usr/bin/python3
"""
Test file for Discount Calculation Module
"""

from discount_calculator import calculate_discount  # Import the function to test

def print_result(result):
    """Print the result of the calculation."""
    print(f"The final price is: {result:.2f}")

if __name__ == "__main__":
    # Test cases to check if the discount is applied correctly
    print_result(calculate_discount(100, 20))  # Expected output: 80.00 (100 - 20% = 80)
    print_result(calculate_discount(200, 15))  # Expected output: 200.00 (no discount applied)
    print_result(calculate_discount(150, 20))  # Expected output: 120.00 (150 - 20% = 120)
    print_result(calculate_discount(50, 50))   # Expected output: 25.00 (50 - 50% = 25)
    print_result(calculate_discount(80, 5))    # Expected output: 80.00 (no discount applied)

    # Additional edge case: zero price
    print_result(calculate_discount(0, 25))    # Expected output: 0.00 (no discount can apply to zero)
    
    # Edge case: 100% discount
    print_result(calculate_discount(100, 100))  # Expected output: 0.00 (100 - 100% = 0)
    
    # Edge case: very small discount
    print_result(calculate_discount(500, 0.01))  # Expected output: 499.95 (500 - 0.01% = 499.95)

