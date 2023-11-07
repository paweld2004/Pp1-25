time_24_hour = input('Enter time (24-hour format): ')

hour, minute = map(int, time_24_hour.split(':'))
period = "am"

if hour >= 12:
    period = "pm"
    if hour > 12:
        hour -= 12

print(f'Time in 12-hour format: {hour}:{minute}{period}')
