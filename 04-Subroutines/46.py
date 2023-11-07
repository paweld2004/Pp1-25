def sum_divisible_by_2_and_3_not_divisible_by_4(x, y):
    total = 0
    for num in range(x, y + 1):
        if num % 2 == 0 and num % 3 == 0 and num % 4 != 0:
            total += num
    return total
