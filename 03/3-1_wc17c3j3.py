# https://dmoj.ca/problem/wc17c3j3

# determine if an input single string satisifes the following requirements
# * must be a string between 8 and 12 characters long (inclusive),
#  every character is either a lowercase letter (a … z), uppercase letter (A … Z), or digit (0 … 9).
#  Furthermore, it must contain:
# at least three lowercase letters,
# at least two uppercase letters, and
# at least one digit.
import sys

VALID = "Valid"
INVALID = "Invalid"

myword = str(input())
upper_count = 0
lower_count = 0
digit_count = 0

for char in myword:
    if char.isupper():
        upper_count = upper_count + 1
    elif char.islower():
        lower_count = lower_count + 1
    elif char.isdigit():
        digit_count = digit_count + 1

if len(myword) < 8 or len(myword) > 12:
    print(INVALID)
elif upper_count >= 2 and lower_count >= 3 and digit_count >= 1:
    print(VALID)
else:
    print(INVALID)
