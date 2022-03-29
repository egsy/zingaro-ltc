# https://dmoj.ca/problem/coci17c1p1

DRAW = "VUCI"
STOP = "DOSTA"
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
DECK = cards * 4
DECK.sort()

hand = int(input())
x = 21

for card in range(hand):
    card = int(input())
    x -= card
    DECK.remove(card)

greater = 0
less = 0

for card in DECK:
    if card > x:
        greater += 1
    elif card <= x:
        less += 1

if greater >= less:
    print(STOP)
elif greater < less:
    print(DRAW)
