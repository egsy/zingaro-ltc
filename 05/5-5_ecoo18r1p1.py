# ecoo18r1p1 ECOO '18 R1 P1 - Willow's Wild Ride
for dataset in range(10):
    info = input().split()
    playtime = int(info[0])
    days = int(info[1])
    box = []

    for day in range(days):
        box.append(input())

    playtime = box.count("B") * playtime
    days = len(box[box.index("B") :])

    # if playtime > days:
    # output = playtime - days
    print(playtime - days)
    # # else:
    #     print(0)
