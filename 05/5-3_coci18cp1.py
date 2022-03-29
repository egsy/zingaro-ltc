# https://dmoj.ca/problem/coci18c2p1
# handle input
A = int(input())
As = []
for num in range(A):
    As.append(int(input()))
print(As)
B = int(input())
Bs = []
for num in range(B):
    Bs.append(int(input()))
print(Bs)
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
turnaround = [False]
score = [0, 0]
lead = ""
prev_lead = ""
for sec in range(0, 2881):
    prev_lead = lead
    if As.count(sec) == 1:
        score[0] += 1
    if Bs.count(sec) == 1:
        score[1] += 1

    if score[0] > score[1]:
        lead = "A"
    elif score[1] > score[0]:
        lead = "B"

    if lead != prev_lead:
        turnaround.append(True)
        print(score, "lead: ", lead)
        print(turnaround, turnaround.count(True))
