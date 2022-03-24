# https://dmoj.ca/problem/ccc19j3
# DMOJ problem ccc19j3, Cold Compress

num = int(input())
i = 0
output = "{} {} "
encoding = ""

for line in range(num):
    text = str(input())
    print(text, type(text))
    while i < len(text):
        # count how many times character at index `i` appears
        count = 1

        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        encoding += output.format(count, text[i])
        print(encoding)
        i += 1
    print(encoding[:-1])

    line += 1
    encoding = ""
