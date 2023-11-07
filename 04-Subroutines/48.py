def is_correct_product_code(product_code):
    if len(product_code) != 4:
        return False
    first_three_digits = int(product_code[:3])
    control_digit = int(product_code[3])
    return first_three_digits % 7 == control_digit
