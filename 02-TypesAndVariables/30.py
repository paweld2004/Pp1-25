import random

dice = random.randint(1, 6)

is_special_number = dice == 1 or dice == 6

print(f'Dice rolled: {dice}')
print(f'Special number: {is_special_number}')
