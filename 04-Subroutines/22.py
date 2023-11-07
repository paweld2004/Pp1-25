def month(n):
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if 1 <= n <= 12:
        return month_names[n - 1]
    else:
        return "Invalid month number"
        
import mymonth

month_number = int(input("Enter month number: "))
month_name = mymonth.month(month_number)
print(f"The name of month {month_number} is {month_name}")
