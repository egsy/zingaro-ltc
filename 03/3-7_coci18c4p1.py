# https://dmoj.ca/problem/coci18c4p1

elder = str(input())
duel_count = int(input())
wizard_count = 1
wizard_history = elder

for i in range(duel_count):
    duel = str(input())
    if duel[-1] == elder:
        elder = duel[-3]
        if elder not in wizard_history:
            wizard_history += duel[-1]
            wizard_count = wizard_count + 1

print(elder)
print(wizard_count)
