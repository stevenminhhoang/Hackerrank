n = int(input())
student_marks = {}
sum = 0
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

for i in student_marks[query_name]:
    sum = sum + i

avg = sum / len(student_marks[query_name])
print("%.2f" % avg)
# print(student_marks[query_name])
# for key, value in student_marks.items():
#     print(key)
#     for i in value:
#         sum = sum + i
#     avg = sum /len(value)
#     # print(student_marks[value])
