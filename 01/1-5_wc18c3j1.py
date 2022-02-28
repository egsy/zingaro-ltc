p = int(input())
b = int(input())
d = int(input())

badges = p // b * d
remainder = p % b

print(badges + remainder)
