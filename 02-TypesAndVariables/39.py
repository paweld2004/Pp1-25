price = float(input('Enter price: '))
discount_percentage = float(input('Enter discount %: '))

discount = (discount_percentage / 100) * price
discounted_price = price - discount

print(f'Price with discount: {discounted_price:.2f}')
print(f'Reduction: {discount:.2f}')
