binary_number = input('Enter binary number: ')

decimal_number = 0
for i in range(len(binary_number)):
    decimal_number += int(binary_number[i]) * (2 ** (3 - i))

print(f'Binary number in decimal notation: {decimal_number}')
