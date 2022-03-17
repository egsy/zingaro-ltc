# DMOJ problem ccc02j2, AmeriCanadian
# https://dmoj.ca/problem/ccc02j2

VOWEL = "aeiouy"
word = ""

while word != "quit!":
    word = str(input())
    if len(word) > 4 and word[-2:] == "or" and word[-3] not in VOWEL:
        word = word[0:-2] + "our"
        print(word)
    elif word != "quit!":
        print(word)
