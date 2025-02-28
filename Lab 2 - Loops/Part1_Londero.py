"""
Part 1: Mod and Integer Division
Question: How can I use mod (%) and integer division (/) to figure out the nth digit of an
Integer?

In part1.py, complete the code so that after it gets a value for "number" and "n" from the
user, it prints out the nth digit (from the right) of the given number.
Again, your solution should use mod (%) and integer division (/) to figure out this nth digit of
the integer. Think about how you can do so.
As an example, if I have number = 123456, I want to be able to use mod and division in some
way to fetch the 1st digit of this number (which is 6), or 2nd (which is 5), or 3rd (which is 4),
etc. using some equation that involves the values of "number" and "n".
"""


print("This program will show the desire decimal number, from the right, to the left of the preference number")

number = int(input("Please, enter the number to find the nth digit of:      "))
n = int(input("Please, enter the number of the desire decimal place:      "))

for x in range(n-1): # -1 for the exact location
    number //= 10
    decimal_number = number % 10

print(f"The nth digit is   -> {decimal_number} <-")
