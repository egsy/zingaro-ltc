# https://dmoj.ca/problem/ccc18j2

n = int(input())
yest = input()
today = input()

occupied = 0

for i in range(len(yest)):
    if yest[i] == "C" and today[i] == "C":
        occupied = occupied + 1
print(occupied)
