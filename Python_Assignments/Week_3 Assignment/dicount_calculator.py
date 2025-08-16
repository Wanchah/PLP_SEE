# CALCULATING DISCOUNT PRICES

def calculate_discount(price, discount_percent):
    """
    Checking the discount percentage if it is 20% or higher.
    Calculates the final price after applying a discount.
    Returns the final price if the discount is applied, otherwise returns the original price.

    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        discounted_price = price - discount_amount
        return f"Discount applied! Final price: {discounted_price:.2f}"
    else:
        return f"No discount applied. Your price remains: {price:.2f}"

# Prompt for user inputs
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function and print the result
print(calculate_discount(price, discount_percent))