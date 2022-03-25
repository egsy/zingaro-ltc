# https://dmoj.ca/problem/ccc19j3
# DMOJ problem ccc19j3, Cold Compress

num = int(input())
i = 0
output = "{} {} "
encoding = ""

for line in range(num):
    text = str(input())

    while i < len(text):
        # count how many times character at index `i` appears
        count = 1

        while i < len(text) - 1 and text[i] == text[i + 1]:
            i += 1
            count += 1
        encoding += output.format(count, text[i])
        i += 1
    print(encoding[:-1])

    # reset variables
    encoding = ""
    i = 0
