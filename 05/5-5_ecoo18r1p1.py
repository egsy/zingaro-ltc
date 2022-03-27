# ecoo18r1p1 ECOO '18 R1 P1 - Willow's Wild Ride
for dataset in range(10):
    info = input().split()
    t = int(info[0])
    n = int(info[1])
    box_time = 0

    for day in range(n):
        day = input()
        if day == "B":
            box_time += t
            box_time -= 1
        else:
            if box_time > 0:
                box_time -= 1

    print(box_time)
