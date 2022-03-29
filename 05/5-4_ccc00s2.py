# ccc00s2 CCC '00 S2 - Babbling Brooks - DMOJ: Modern Online Judge

streams = [0]

n = int(input())
for flow in range(n):
    streams.append(int(input()))

done = False

while not done:
    code = int(input())
    if code == 77:
        done = True
    # split
    if code == 99:
        num = int(input())
        # the percentage of flow from the
        # split stream that flows to the left fork.
        # The rest flows to the right fork)
        flow_percentage = int(input())
        split_left = round((streams[num] * flow_percentage) / 100)
        split_right = streams[num] - split_left

        streams.insert(num, 0)
        streams[num] = split_left
        streams[num + 1] = split_right

    # join
    if code == 88:
        num = int(input())
        # a line containing an integer, the number of the stream 
        # that is rejoined with the stream to its right
        streams[num] += streams[num + 1]
        streams.pop(num + 1)

print(*streams[1:])
