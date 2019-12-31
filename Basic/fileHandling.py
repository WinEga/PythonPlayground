
# File handling in Python

with open('Test.txt', 'r') as rf:
    for line in rf:
        print(line, end='')

with open('Test.txt', 'r') as rf:
    with open('Test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
        wf.write('\nFile copy is completed')

with open('Python_PL.png', 'rb') as rf:
    with open('Python_PL_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)
print('\n\nImage copy is completed')
