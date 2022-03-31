# /ecoo19r1p1 ECOO '19 R1 P1 - Free Shirts - DMOJ: Modern Online Judge
for i in range(3):
    data = input()
    data = data.split()
    for i in range(len(data)):
        data[i] = int(data[i])

    # `N` - the initial number of shirts that Ian has,
    # `M` the number of events coming up, and
    # `D` the number of days, respectively.

    N = [data[0]]
    M = data[1]
    D = data[2]

    # next line contains `M`  integers A i A_i ( 1 ≤ A i ≤ D ) (1 \le A_i \le D) ,
    # the days on which there are events. There may be multiple events in a single day.
    event_days = input()
    event_days = event_days.split()
    for i in range(len(event_days)):
        event_days[i] = int(event_days[i])

    # For each dataset, output the number of times
    # Ian will do the laundry in the next D D days.
    wash_count = 0
    clean_shirt = int(N[0])
    idx = 0
    for i in range(1, D + 1):
        if clean_shirt == 0:
            wash_count += 1
            clean_shirt = sum(N)
            print(f"day {i} laundry day - washed {wash_count} times")

        clean_shirt -= 1

        # if event_days.count(i) > 0:
        #     print(f"day {i}")
        #     # handle multiple events on one day
        #     clean_shirt += 1 * event_days.count(i)
        #     N.append(event_days.count(i))

        # print(f"{new_shirt} new shirt(s)! now {clean_shirt} clean shirts left")

        while idx < len(event_days) and event_days[idx] == i:
            clean_shirt += 1
            N.append(1)
            idx += 1

        # if event_days.count(i) > 0:
        #     # handle multiple events on one day
        #     new_shirt = 1 * event_days.count(i)
        #     print(f"day {i} {new_shirt} new shirt(s)! {clean_shirt} shirts left")

    print(wash_count)
