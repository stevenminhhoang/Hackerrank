t = int(input())
result = []
for _ in range(t):
    numA = input()
    a = set(map(int, input().split()))
    numB = input()
    b = set(map(int, input().split()))
    if a.issubset(b):
        result.append(True)
    else:
        result.append(False)

for i in result:
    print(i)
