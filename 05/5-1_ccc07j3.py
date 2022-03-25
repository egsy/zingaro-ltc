# DMOJ problem ccc07j3, Deal or No Deal Calculator

briefcases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
print(briefcases)

num = int(input())

for i in range(num):
    eliminated = int(input()) - 1
    briefcases[eliminated] = 0
print(briefcases)

average = sum(briefcases) / (len(briefcases) - briefcases.count(0))
offer = int(input())
if offer > average:
    print("deal")
else:
    print("no deal")
