# https://dmoj.ca/problem/ccc20j2
# When a person has a disease, they infect exactly R other people but only on the very next day.
# No person is infected more than once. We want to determine when a total of more than P people have had the disease.

# Input Specification

# There are three lines of input. Each line contains one positive integer.
# The first line contains the value of P .
# The second line contains N , the number of people who have the disease on Day 0 0 .
# The third line contains the value of R .
# Assume that P ≤ 10^7 and N ≤ P and R ≤ 10 .

p = int(input())  # population
n = int(input())  # number infected on day 0
r = int(input())  # reproduction number
day = 0
infected = n

while n <= p:
    n = n + infected * r
    infected = infected * r
    day += 1

print(day)
