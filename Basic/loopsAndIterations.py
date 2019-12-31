
list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in list_numbers:
    if num == 5:
        print("We found the number 5...!")
    print(num)

for num in list_numbers:
    if num == 5:
        print("We found the number 5...!")
        break
    print(num)

for num in list_numbers:
    if num == 5:
        print("We found the number 5...!")
        continue
    print(num)

for num in range(1, 11):
    print(num)

x = 1
while x < 5:
    print(x)
    x += 1

