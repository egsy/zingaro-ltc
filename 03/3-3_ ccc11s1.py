# https://dmoj.ca/problem/ccc11s1
# write program that distinguishes English text from French text

ENGLISH = "English"
FRENCH = "French"

lines = int(input())
s_count = 0
t_count = 0
text = ""
for i in range(lines):
    text = text + str(input())

t_count = text.count("t") + text.count("T")
s_count = text.count("s") + text.count("S")

if t_count > s_count:
    print(ENGLISH)
elif s_count > t_count:
    print(FRENCH)
elif t_count == s_count:
    print(FRENCH)
