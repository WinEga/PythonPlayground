"""
Write a python to print the below pattern using for loop

*	*	*	*	*
*		*		*
*		*		*
*	*	*	*	*

"""
for row in range(4):
    for column in range(5):
        if row == 1 and (column == 1 or column == 3):
            print("\t", end="")
            continue
        if row == 2 and (column == 1 or column == 3):
            print("\t", end="")
            continue
        print("*\t", end="")
    print()
