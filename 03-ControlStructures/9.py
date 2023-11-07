total_tasks = int(input('Enter the total number of tasks: '))
correct_tasks = int(input('Enter the number of correctly completed tasks: '))

if correct_tasks >= total_tasks * 0.5:
    print('Test passed')