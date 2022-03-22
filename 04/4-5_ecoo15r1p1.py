# DMOJ problem ecoo15r1p1, When You Eat Your Smarties

red = 0
orange = 0
blue = 0
green = 0
yellow = 0
pink = 0
violet = 0
brown = 0
color = ""
i = 0
handful = 0


for i in range(10):
    print(i)
    color = str(input())
    while color is True:
        if color == "red":
            red += 1
        elif color == "orange":
            orange += 1
        elif color == "blue":
            blue += 1
        elif color == "green":
            green += 1
        elif color == "yellow":
            yellow += 1
        elif color == "pink":
            pink += 1
        elif color == "violet":
            violet += 1
        elif color == "brown":
            brown += 1

        groups = [red, orange, blue, green, yellow, pink, violet, brown]
        # for x in range(groups):
        #     if x % 7 == 0
        if color == "end of box":
            # do math, output seconds
            # print(handful)
            i += 1
            print(groups)
