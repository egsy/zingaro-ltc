# https://dmoj.ca/problem/dmopc16c1p0

ABSOLUTELY = "absolutely"
FAIR = "fairly"
VERY = "very"
OUTPUT = "C.C. is M satisfied with her pizza."

width = int(input())
cheesiness = int(input())

if width == 3 and cheesiness >= 95:
    print(OUTPUT.replace("M", ABSOLUTELY))
elif width == 1 and cheesiness <= 50:
    print(OUTPUT.replace("M", FAIR))
else:
    print(OUTPUT.replace("M", VERY))
