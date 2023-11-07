def minimum_coins(amount_to_pay):
    coins = [5, 2, 1]
    count = 0
    for coin in coins:
        while amount_to_pay >= coin:
            amount_to_pay -= coin
            count += 1
    return count

print(minimum_coins(23))  # 6
print(minimum_coins(8))   # 3
print(minimum_coins(2))   # 1
print(minimum_coins(0))   # 0
