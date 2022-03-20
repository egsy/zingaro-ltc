# DMOJ problem ecoo13r1p1, Take a Number

current = int(input())
status = ""
i = 0
j = 0
output = "{} {} {}"
while status != "EOF":
    status = input(str())
    if status == "TAKE":
        i += 1
    elif status == "SERVE":
        j += 1
    elif status == "CLOSE":
        # print(current)
        current = current + i
        print(output.format(i, (i - j), current))
        i = 0
        j = 0
