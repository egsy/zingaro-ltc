# DMOJ problem coci08c1p2, Ptice
# Write a program that, given the correct answers to the exam, determines who of the three was right –
# whose sequence contains the most correct answers.

ADRIAN = "ABCABCABCABC"
BRUNO = "BABCBABCBABC"
GORAN = "CCAABBCCAABB"

num = int(input())
key = str(input())

# adjust length of answer sequences to match length of input
if len(ADRIAN) < num:
    ADRIAN = ADRIAN * (num // len(ADRIAN)) + ADRIAN[: (num % len(ADRIAN))]
    BRUNO = BRUNO * (num // len(BRUNO)) + BRUNO[: (num % len(BRUNO))]
    GORAN = GORAN * (num // len(GORAN)) + GORAN[: (num % len(GORAN))]

# compare answer sequences with given key and count correct answers for each
adrian_count = 0
bruno_count = 0
goran_count = 0
i = 0
while i < num:
    if key[i] == ADRIAN[i]:
        adrian_count += 1
    if key[i] == BRUNO[i]:
        bruno_count += 1
    if key[i] == GORAN[i]:
        goran_count += 1

    i += 1

# compare correct counts and prepare output
most = adrian_count
if bruno_count > most:
    most = bruno_count
if goran_count > most:
    most = goran_count

print(most)
if adrian_count == most:
    print("Adrian")
if bruno_count == most:
    print("Bruno")
if goran_count == most:
    print("Goran")
