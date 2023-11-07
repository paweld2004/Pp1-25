current_price = 140.00
previous_price = 200.00

if (previous_price - current_price) >= 0.1 * previous_price:
    print('Buy the product!!')
    reduction_percent = ((previous_price - current_price) / previous_price) * 100
    print(f'Product price reduced by {reduction_percent:.2f}%')
