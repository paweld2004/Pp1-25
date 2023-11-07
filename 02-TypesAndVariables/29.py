import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)
dice_sum = dice1 + dice2 + dice3

print(f'Dice 1: {dice1}')
print(f'Dice 2: {dice2}')
print(f'Dice 3: {dice3}')
print(f'Sum of dice rolled: {dice_sum}')
