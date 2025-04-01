#!/usr/bin/python3
"""
Discount Calculation Module
"""

def calculate_discount(price, discount_percent):
    """ 
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply the discount. 
    Otherwise, return the original price.
    
    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to apply.

    Returns:
        float: The final price after the discount (or original price if no discount).
    """
    
    # Check if the discount is 20% or more
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        # Subtract the discount from the original price to get the final price
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price


if __name__ == "__main__":
    # Prompt user for input
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Call calculate_discount function to compute the final price
    final_price = calculate_discount(price, discount_percent)
    
    # Print the final price
    print("The final price is: {:.2f}".format(final_price))

