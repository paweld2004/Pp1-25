first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))

if first_number > second_number:
    first_number, second_number = second_number, first_number

print(f'Numbers in ascending order: {first_number}, {second_number}')
