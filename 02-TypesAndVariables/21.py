height_cm = int(input('Enter your height in cm: '))

feet = height_cm // 30.48
inches = (height_cm % 30.48) / 2.54

print(f'I am {height_cm}cm tall, i.e. {feet} feet and {inches:.0f} inches')
