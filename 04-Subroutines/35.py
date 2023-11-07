def perform_arithmetic_operation(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2
    else:
        return None

print(perform_arithmetic_operation(2, 3, "+"))   # 5
print(perform_arithmetic_operation(2, 3, "%"))   # 2
print(perform_arithmetic_operation(2, 3, "**"))  # 8
print(perform_arithmetic_operation(2, 3, "*"))   # 6
print(perform_arithmetic_operation(2, 3, "-"))   # -1
