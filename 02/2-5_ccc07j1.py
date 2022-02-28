# https://dmoj.ca/problem/ccc07j1
# Write a program that reads in three weights and
# prints out the weight of Mama Bear's bowl (middle).
# You may assume all weights are positive integers less than 100.

bowl_A = int(input())
bowl_B = int(input())
bowl_C = int(input())

list = [bowl_A, bowl_B, bowl_C]
list.sort()
print(list.pop(1))
