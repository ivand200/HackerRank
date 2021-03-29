# Python If-Else
# Task
# Given an integer,n , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

import math
import os
import random
import re
import sys

n = int(raw_input().strip())
    if (n % 2) == 1:
        print('Weird')
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

# Task
# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# V1
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)
#V2
a = int(input())
b = int(input())
print("{0}\n{1}\n{2}".format((a + b), (a - b), (a * b)))

# Task
# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  a//b .
# The second line should contain the result of float division, a / b.
# No rounding or formatting is necessary.
# Example
# a = 3
# b = 5
# The result of the integer division 3//5 = 0.
# The result of the float division is 3/5 = 0.6.
# Ver2 print("{0}\n{1}".format(a//b, a/b))
a = int(input())
    b = int(input())
    int_div = a // b
    div = a / b
    print(f"{int_div}\n{div}")

# Task
# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i**2.
# Example
# n = 3
# The list of non-negative integers that are less than n = 3 is [0,1,2]. Print the square of each number on a separate line.

0
1
4
n = int(input())
for i in range(0, n):
        square = i ** 2
        print(square)
# print(*[num**2 for num in range(n)], sep='\n')

# An extra day is added to the calendar almost every four years as February 29,
# and the day is called a leap day. It corrects the calendar for the fact that
# our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
# In the Gregorian calendar, three conditions are used to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
# while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source
# Task
# Given a year, determine whether it is a leap year. If it is a leap year,
# return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments
# to the is_leap function. It is only necessary to complete the is_leap function.

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
