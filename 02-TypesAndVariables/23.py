a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

circumference = a + b + c

print(f'Triangle area: {area:.2f}')
print(f'Triangle circumference: {circumference:.2f}')
