def sum_natural_numbers(n):
    if n == 1:
        return 1
    return n + sum_natural_numbers(n - 1)
