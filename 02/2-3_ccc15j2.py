# https://dmoj.ca/problem/ccc15j2

HAPPY = ":-)"
SAD = ":-("

message = input(str())
happy_count = message.count(HAPPY)
sad_count = message.count(SAD)

if not (HAPPY or SAD) in message:
    print("none")
elif happy_count == sad_count and :
    print("unsure")
elif happy_count > sad_count:
    print("happy")
else:
    print("sad")
