apple_3 = int(input())
apple_2 = int(input())
apple_1 = int(input())

banana_3 = int(input())
banana_2 = int(input())
banana_1 = int(input())

apple_total = apple_1 + (apple_2 * 2) + (apple_3 * 3)
banana_total = banana_1 + (banana_2 * 2) + (banana_3 * 3)

if apple_total > banana_total:
    print('A')
elif banana_total > apple_total:
    print("B")
else:
    print('T')
