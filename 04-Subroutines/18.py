def numbers(n):
    return ' '.join(map(str, range(1, n + 1)))

numbers_1_to_15 = numbers(15)
numbers_1_to_7 = numbers(7)

print(f"Numbers <1,15>: {numbers_1_to_15}")
print(f"Numbers <1,7>: {numbers_1_to_7}")
