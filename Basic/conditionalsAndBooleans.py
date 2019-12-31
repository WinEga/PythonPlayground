# Python will not support switch cases. it will be handled in elif

programme_language = 'Kotlin'

if programme_language == 'Python':
    print("The language is Python")
elif programme_language == 'Java':
    print("The language is Java")
elif programme_language == 'Kotlin':
    print("The language is Kotlin")
else:
    print("No matches found")

# if statement with 'and', 'or' & 'not' conditions
user = 'Admin_1'
is_logged_in = True

if user == 'Admin_1' and is_logged_in:
    print("User in home page")
else:
    print("Invalid user")

if user == 'Admin_1' or is_logged_in:
    print("User in home page")
else:
    print("Invalid user")

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

if list1 == list2:
    print("list1 and list2 are same")

print(id(list1))
print(id(list2))

if list1 is list2:
    print("list1 and list2 are same in the same memory location")