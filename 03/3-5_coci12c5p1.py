# https://dmoj.ca/problem/coci12c5p1
# write a program to determine if a composition is more likely written in
# A-minor or C-major

A_MIN = "A-mol"
C_MAJ = "C-dur"

a_min_tones = "ADE"
c_maj_tones = "CFG"

composition = input(str())
a_min_count = 0
c_maj_count = 0

for char in range(len(composition)):
    if char == 0 or composition[char - 1] == "|":
        if composition[char] in a_min_tones:
            a_min_count = a_min_count + 1
        if composition[char] in c_maj_tones:
            c_maj_count = c_maj_count + 1

if a_min_count > c_maj_count:
    print(A_MIN)
elif a_min_count < c_maj_count:
    print(C_MAJ)
elif a_min_count == c_maj_count:
    if composition[-1] == "C":
        print(C_MAJ)
    else:
        print(A_MIN)
