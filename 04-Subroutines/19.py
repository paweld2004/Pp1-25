def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == "__main__":
    print(sum_digits(7182))
    print(sum_digits(0))
    print(sum_digits(333))

import digits

number = int(input("Enter a number: "))
sum_d = digits.sum_digits(number)
msg = f"Sum of digits {number} is {sum_d}"
print(msg)
