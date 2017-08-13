students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    student = [name, score]
    students.append(student)
    students = sorted(students, key=lambda x: x[1])
    scores = sorted(set(x[1] for x in students))

for name in sorted(x[0] for x in students if x[1] == scores[1]):
    print(name)
