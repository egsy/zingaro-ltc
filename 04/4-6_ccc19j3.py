# https://dmoj.ca/problem/ccc19j3
# DMOJ problem ccc19j3, Cold Compress

num = int(input())
i = 0
output = "{} {}"

for line in range(num):
    text = str(input())
    while i < len(text):
        # count how many times character at index `i` appears
        count = 1

        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        print(output.format(count, text[i]))
        i += 1
    line += 1
