# https://dmoj.ca/problem/coci12c5p1
# write a program to determine if a composition is more likely written in
# A-minor or C-major

A_MIN = "A-mol"
C_MAJ = "C-dur"

a_min_tones = "ADE"
c_maj_tones = "CFG"

composition = input(str())
accented = composition[0]

for char in range(len(composition)):
    if composition[char] == "|":
        accented = accented + composition[char + 1]
    elif composition[char] != "|":
        continue

a_min_count = 0
c_maj_count = 0

for note in range(len(accented)):
    if accented[note] in a_min_tones:
        a_min_count = a_min_count + 1
    if accented[note] in c_maj_tones:
        c_maj_count = c_maj_count + 1

if a_min_count > c_maj_count:
    print(A_MIN)
elif a_min_count < c_maj_count:
    print(C_MAJ)
elif a_min_count == c_maj_count:
    if accented[-1] == "C":
        print(C_MAJ)
    elif accented[-1] == "A":
        print(A_MIN)
