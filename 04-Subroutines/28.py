def is_valid_binary(binary_number):
    return all(bit in '01' for bit in binary_number)

print(f('101101'))  # True
print(f('1311a10100'))  # False
