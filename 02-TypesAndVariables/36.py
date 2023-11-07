buy_rate = float(input('Bank buys EUR: '))
sell_rate = float(input('Bank sells EUR: '))

spread = sell_rate - buy_rate

print(f'Spread: {spread:.4f}')
