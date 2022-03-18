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

# compare answer sequences with given key
j = 0
i = 0
while i <= num:
    print(key[i])
    if key[i] == ADRIAN[i]:
        print("adrian match")

    i += 1
