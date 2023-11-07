name = input('Enter your name: ')

for letter in name:
    numeric_representation = ord(letter)
    print(f'{letter}({numeric_representation})')
