sum = 0
count = 0

while True:
    num = int(input('Enter number: '))
    if num == 0:
        break
    sum += num
    count += 1

mean = sum / count if count > 0 else 0
print(f'RESULT: Quantity={count}, Sum={sum}, Mean={mean}')
