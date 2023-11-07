amount_in_pln = int(input('Enter the amount in PLN: '))

coins_5 = amount_in_pln // 5
amount_in_pln %= 5
coins_2 = amount_in_pln // 2
amount_in_pln %= 2

print(f'The amount of PLN {amount_in_pln} in coins:\n5 zł – {coins_5}\n2 zł – {coins_2}\n1 zł – {amount_in_pln}')
