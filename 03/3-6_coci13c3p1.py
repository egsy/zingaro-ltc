# https://dmoj.ca/problem/coci13c3p1
# 0 1   A
# 1 1   B
# 2 2   BA
# 3 3   BAB
# 4 5   BABBA
# 5 8   BABBABAB
# 6 13  BABBABABBABBA
# When he saw this, Mirko realized that the machine alters the word in a way that
# all the letters B get transformed to BA and all the letters A get transformed to B.

fibo = [0, 1]
button = int(input())

for i in range(0, button):
    n = fibo[-1] + fibo[-2]
    fibo.append((n))

print(fibo[-3], fibo[-2])
