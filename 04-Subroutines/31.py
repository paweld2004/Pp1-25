def count_negative_even_numbers(x, y):
    return sum(1 for num in range(x, y) if num < 0 and num % 2 == 0)

print(count_negative_even_numbers(-7, 8))  # 3
print(count_negative_even_numbers(-1, 11)) # 0
