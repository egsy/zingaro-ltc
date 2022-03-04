# https://dmoj.ca/problem/ccc11s2
# write a program that can be used to grade a multiple choice test
# The input will contain the number  N ( 0 < N < 10 000 0 < N < 10\,000 ) followed by 2N lines.
# The 2N lines are composed of N N lines of student responses (with one of A, B, C, D or E on each line),
# followed by N lines of correct answers (with one of A, B, C, D or E on each line),
# if line i is the student response, then line N+i will contain the correct answer to that question).
#
# Output the integer ( 0 ≤ C ≤ N ) which corresponds to the number of questions the student answered correctly.

lines = int(input())
correct = ""
student = ""

grade = 0

for i in range(lines * 2):
    if i < lines:
        correct = correct + str(input())
    elif i >= lines:
        student = student + str(input())

for answer in range(len(correct)):
    if correct[answer] == student[answer]:
        grade = grade + 1

print(grade)
