# https://dmoj.ca/problem/coci18c3p1
# determine maximum number of times the string "HONI" appears in input

HONI = "HONI"
string = str(input())
honi_count = 0
char = 0
letter = 0

for char in range(len(string)):
    if string[char] == HONI[letter]:
        letter = letter + 1
        if letter == 4:
            letter = 0
            honi_count = honi_count + 1
print(honi_count)
