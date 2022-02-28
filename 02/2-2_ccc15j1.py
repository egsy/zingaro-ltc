# https://dmoj.ca/problem/ccc15j1

BEFORE = "Before"
AFTER = "After"
SPECIAL = "Special"

# program that takes input for a numerical month and numerical
# day of the month and then determines whether that date occurs
# before, after, or on February 18

month = int(input())
day = int(input())

if month < 2 or (month == 2 and day < 18):
    print(BEFORE)
elif month > 2 or (month == 2 and day > 18):
    print(AFTER)
else:
    print(SPECIAL)
