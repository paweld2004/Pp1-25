def generate_number_string(n):
    return ''.join(str(i) for i in range(1, n + 1))

print(generate_number_string(11)) # "1234567891011"
print(generate_number_string(4))  # "1234"
