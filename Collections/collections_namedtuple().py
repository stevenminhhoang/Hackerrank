from collections import namedtuple

n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)
student_marks = []

for _ in range(n):
    argv = input().split()
    s = Student(*argv)
    student_marks.append(int(s.MARKS))

print(round(sum(student_marks)/ n, 2))
