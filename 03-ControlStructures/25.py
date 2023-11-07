num_products = int(input('Number of products purchased: '))
product_price = float(input('Product price: '))

if num_products > 2:
    discount = 0.25 
    discount = 0

amount_to_pay = num_products * product_price * (1 - discount)

print(f'Amount to pay: {amount_to_pay:.2f}')
