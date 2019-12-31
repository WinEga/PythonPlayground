
# Dictionaries, we can have keys and values. Below are few examples

employees = {'Name': 'Win', 'Age': 28, 'Role': ['Tester', 'SME', 'PO']}

print(employees)

# Re-assign the name
employees['Name'] = 'Ega'

# Re-assign the age
employees['Age'] = 29

print(employees)

# update name and age
employees.update(Name='ML', Age=19)

print(employees)

for keys in employees:
    print(keys)

for keys, values in employees.items():
    print(keys, values)
