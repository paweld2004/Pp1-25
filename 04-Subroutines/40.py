def sum_repeated_digits(number):
    number_str = str(number)
    unique_digits = set(number_str)
    total = 0
    for digit in unique_digits:
        count = number_str.count(digit)
        if count > 1:
            total += int(digit) * count
    return total
