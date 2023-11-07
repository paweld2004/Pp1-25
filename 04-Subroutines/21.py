import random

def generate_number():
    return random.randint(1, 9)
    
import mymath
import mykeyboard

user_number = mykeyboard.read_number()
computer_number = mymath.generate_number()

print(f"Computer number: {computer_number}")

if user_number == computer_number:
    print("You won the game!!")
else:
    print("You lost the game.")
