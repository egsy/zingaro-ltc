# https://dmoj.ca/problem/coci18c2p1
# handle input
A = int(input())
As = []
for num in range(A):
    As.append(int(input()))

B = int(input())
Bs = []
for num in range(B):
    Bs.append(int(input()))

# calculate how many points scored in first half-time
# game lasts 4x12 min, so half game = 24 min = 1440 sec
points = 0
for sec in range(0, 1441):
    if As.count(sec) == 1:
        print(sec)
        points += 1
    if Bs.count(sec) == 1:
        print(sec)
        points += 1
print(points)

# count turnarounds in the match
for sec in range(0,2881):
    