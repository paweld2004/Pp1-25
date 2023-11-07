height_cm = float(input('Enter your height in cm: '))
weight_kg = float(input('Enter your weight in kg: '))

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

is_correct_weight = 18.5 <= bmi <= 24.9

print(f'Your BMI index: {bmi:.2f}')
print(f'Correct weight: {is_correct_weight}')
