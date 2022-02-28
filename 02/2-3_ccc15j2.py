# https://dmoj.ca/problem/ccc15j2

HAPPY = ":-)"
SAD = ":-("

message = input(str())
happy_count = message.count(HAPPY)
sad_count = message.count(SAD)

if happy_count == sad_count and (happy_count and sad_count > 0):
    print("unsure")
elif happy_count > sad_count:
    print("happy")
elif happy_count < sad_count:
    print("sad")
else:
    print("none")
