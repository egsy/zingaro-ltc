# https://dmoj.ca/problem/ccc11s1
# write program that distinguishes English text from French text

from black import out


ENGLISH = "English"
FRENCH = "French"

lines = int(input())
s_count = 0
t_count = 0
text = ""
for i in range(lines):

    text = text + str(input())
print(text)

for char in text:
    if char == "t":
        t_count = t_count + 1
print(t_count)
