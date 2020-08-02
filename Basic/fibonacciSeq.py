# Program to display the Fibonacci sequence up-to nth term
# Ega Learning Curve UK, https://www.youtube.com/channel/UCTmehr9p2PDXN0i_D1FA1QQ


nterms = int(input("How many terms to be Printed of Fibonacci sequence? "))

# first two terms
F0, F1 = 0, 1
count = 0

# check if the number of terms is valid or not
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence up-to", nterms, ":")
    print(F0)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(F0)
        nth = F0 + F1
        # update values
        F0 = F1
        F1 = nth
        count += 1

