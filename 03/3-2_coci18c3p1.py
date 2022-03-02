# https://dmoj.ca/problem/coci18c3p1
# determine maximum number of times the string "HONI" appears in input

HONI = "HONI"
string = str(input())
honi_count = 0
char = 0
letter = 0

for char in range(len(string)):
    for letter in range(len(HONI)):
        if string[char] == HONI[letter]:
            char = char + 1
            letter = letter + 1
        elif string[char] == HONI[letter] and letter == 3:
            char = char + 1
            letter = 0
            honi_count = honi_count + 1
    # for i in range(len(HONI)):
    #     if i < 3 and string[char] == HONI[i]:
    #         i = i + 1
    #     elif i == 3 and string[char] == HONI[i]:
    #         honi_count = honi_count + 1
    #     elif i > 3:
    #         i = 0

print(honi_count)
