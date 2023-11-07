personal_data = "Mr. John May, born on 1998-02-16"

parts = personal_data.split(', ')
name = parts[0].split(' ')[1]
surname = parts[0].split(' ')[2]
initials = name[0] + surname[0]
birth_date = parts[1]

print(f'Description: {personal_data}')
print(f'Name: {name}')
print(f'Surname: {surname}')
print(f'Initials: {initials}')
print(f'Born: {birth_date}')
