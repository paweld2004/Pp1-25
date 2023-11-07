for i in range(1, 31):
    result = ''
    if i % 3 == 0:
        result += 'THREE '
    if i % 5 == 0:
        result += 'FIVE '
    if not result:
        result = i
    print(result, end=' ')
