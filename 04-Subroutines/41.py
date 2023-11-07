def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    candidate = 2
    while count < n:
        if is_prime(candidate):
            count += 1
        candidate += 1
    return candidate - 1
