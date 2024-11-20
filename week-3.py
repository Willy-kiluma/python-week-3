def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Apply the discount
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price



original_price = 100
discount = 25
final_price = calculate_discount(original_price, discount)
print(final_price)

original_price = 100
discount = 15
final_price = calculate_discount(original_price, discount)
print(final_price) 
