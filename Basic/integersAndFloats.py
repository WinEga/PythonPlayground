#  This is to understand integers and Floats in Python

num_1 = 3

num_2 = 3.14

print(type(num_1))
print(type(num_2))


# Arithmetic operations: /, *, +, -, %, //

print(3 / 2)  # Division
print(3 * 2)  # Multiplication
print(3 + 2)  # Addition
print(3 - 2)  # Subtraction
print(3 % 2)  # Modulus
print(3 ** 2)  # Exponent
print(33 // 2)  # Floor Division

# Comparisons operators, ==, !=, >, <, >=, <=

print(num_1 == num_2)  # Is Equal
print(num_1 != num_2)  # Is Not Equal
print(num_1 > num_2)  # Is Greater Than
print(num_1 < num_2)  # Is Less Than
print(num_1 >= num_2)  # Is Greater Than or Equal to
print(num_1 <= num_2)  # Is Less Than or Equal to

num_str1 = '50'
num_str2 = '40'

print(num_str1 + num_str2)  # it works as concatenation

print(int(num_str1) + int(num_str2))  # convert string into Integer and then adds

