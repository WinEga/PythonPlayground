"""This programme to understand the basics of string format"""
print("Welcome Dear Team")

print("Maths\n"*5)

full_name = 'Egambaram Panneerselvam'

age = 29

is_new_user = False

full_message = 'Full name: {}, Age: {}, New User Status: {}, Welcome'.format(full_name, age, is_new_user)

full_message_f = f'Full name: {full_name}, Age: {age}, New User Status: {is_new_user}, Welcome'

print(full_message)
print(full_message_f)

message = 'Welcome to the Python leaning sessions'
print(message[0])  # To print the first char of the message
print(message[-1])  # To print the last char of the message
print(message[0:7])  # To print the range of chars. it includes the first char and excludes the upper bound chars
print(len(message))  # To print the the total number of chars
split = message.split()  # To split the message based on whitespace
print(split)  # To print array of message from split
print(split[0])  # To print the first string of the split message
print(split[-1])  # To print the last string of the split message
print(message.upper())
print(message.lower())
print(help(str.upper))
print(message.title())
print(message.capitalize())
print(message.istitle())
print(message.find("welcome"))
print(message.index("Welcome"))
