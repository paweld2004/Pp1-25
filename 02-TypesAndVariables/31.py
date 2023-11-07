import random

computer_number = random.randint(1, 6)

user_guess = int(input('Guess a number from 1 to 6: '))

is_correct_guess = user_guess == computer_number

print(f'Computer rolled: {computer_number}')
print(f'User guessed correctly: {is_correct_guess}')
