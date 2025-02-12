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


n = int(input("# rows: "))  #input the rows
#_____________EXAMPLE_____
for how_many_rows in range(1, n + 1):   # X axis
    for y in range(how_many_rows):# Y axis
        print("*", end="")
    print()

print()
#_________________________
# pattern 1
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")  # Print spaces for alignment
    for j in range(2 * i + 1):
        print("*", end="")  # Print stars
    print()

print()  # Separate patterns
# pattern 2
for i in range(n, 0, -1):  # Start from n and decrease
    for j in range(i):
        print("*", end="")  # Print stars with spaces
    print()
print()
#_________________________
# pattern 3
# X X X X X
# pattern 4
# X X X X X
#_________________________
# pattern 5
for i in range(1, n + 1, 2):  # Upper half (including middle)
    for j in range((n - i) // 2):
        print(" ", end="")  # Print spaces for alignment
    for j in range(i):
        print("*", end="")  # Print stars
    print()

for i in range(n - 2, 0, -2):  # Lower half
    for j in range((n - i) // 2):
        print(" ", end="")  # Print spaces for alignment
    for j in range(i):
        print("*", end="")  # Print stars
    print()