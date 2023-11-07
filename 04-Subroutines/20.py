def read_number():
    return int(input("Enter a number: "))

if __name__ == "__main__":
    number1 = read_number()
    number2 = read_number()
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
