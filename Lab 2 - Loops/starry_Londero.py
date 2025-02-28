"""
Part 2: Star Drawings with Nested Loops

Take a look at starry.py posted on our course website. Take some time looking through the
code, explaining how it works.
Add your explanation as in-line comments if needed.
Once you feel completely confident in your understanding of starry.py, comment out the
given loop and add in other loops which draw at least three of the following drawings (n
should be the # of rows for each of them). If you choose any of the last three, decide what
you want to do it if n is even.
"""
"""
You are only allowed to use the following 3 print functions.
print()
print(" ", end="")
print("*", end="")
"""

n = int(input("# rows: "))  # Input the rows
#________EXAMPLE__________
for i in range(1, n + 1):
    for y in range(i):
        print("*", end="") # Print stars
    print()
print()

#_________________________
# pattern 1
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="") # Space
    for j in range(2 * i + 1):
        print("*", end="")
    print()
print()

# pattern 2
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
print()

#_________________________
# pattern 3
# X X X X X
# pattern 4
# X X X X X
#_________________________

# pattern 5
for i in range(1, n + 1, 2):
    for j in range((n - i) // 2):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
# Lower Half
for i in range(n - 2, 0, -2):
    for j in range((n - i) // 2):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()