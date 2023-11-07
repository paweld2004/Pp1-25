def is_within_range(number, x, y):
    return x <= number <= y

import mynumber

number = int(input("A number: "))
x = 2
y = 15

if mynumber.is_within_range(number, x, y):
    print(f"Number {number} in the range <{x},{y}>: yes")
else:
    print(f"Number {number} in the range <{x},{y}>: no")
