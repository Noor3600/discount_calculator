# Step 1: Define the function calculate_discount
def calculate_discount(price, discount_percent):
    # Step 2: Check if discount is 20% or higher
    if discount_percent >= 20:
        # Apply discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # No discount, return the original price
        return price

# Step 3: Prompt user for the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Step 4: Calculate the final price using the function
final_price = calculate_discount(price, discount_percent)

# Step 5: Print the final price
print(f"The final price is: ${final_price:.2f}")