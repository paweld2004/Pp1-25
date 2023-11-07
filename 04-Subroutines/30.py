def sum_digits(number, even):
    number_str = str(number)
    if even:
        digits = [int(digit) for digit in number_str if int(digit) % 2 == 0]
    else:
        digits = [int(digit) for digit in number_str if int(digit) % 2 != 0]
    return sum(digits)

print(sum_digits(3124, True))   # 6
print(sum_digits(3124, False))  # 4
print(sum_digits(20576, False)) # 12
print(sum_digits(20576, True))  # 8
print(sum_digits(13115, True))  # 0
