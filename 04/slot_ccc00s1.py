# https://dmoj.ca/problem/ccc00s1

output = "Martha plays {} times before going broke."
quarters = int(input())
first = int(input())
second = int(input())
third = int(input())

plays = 0
machine = 0

while quarters >= 1:
    quarters -= 1

    if machine == 0:
        first += 1
        if first == 35:
            first = 0
            quarters += 30
    elif machine == 1:
        second += 1
        if second == 100:
            second = 0
            quarters += 60
    elif machine == 2:
        third += 1
        if third == 10:
            third = 0
            quarters += 9

    plays += 1
    machine += 1

    if machine == 3:
        machine = 0

print(output.format(plays))
