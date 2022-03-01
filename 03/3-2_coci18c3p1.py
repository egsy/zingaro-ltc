# https://dmoj.ca/problem/coci18c3p1
# determine maximum number of times the string "HONI" appears in input

HONI = "HONI"
string = str(input())
honi_count = 0

for char in range(len(string)):
    print(string[char])
    for i in range(len(HONI)):
        print(string[char], HONI[i])
        if i < 3 and string[char] == HONI[i]:
            i = i + 1
        elif i == 3 and string[char] == HONI[i]:
            honi_count = honi_count + 1
        i = 0
            
print(honi_count)
