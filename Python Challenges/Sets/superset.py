a = set(map(int, input().split()))
n = int(input())
result = []
for _ in range(n):
    b = set(map(int, input().split()))
    if a.issuperset(b) and len(a.difference(b)) > 0:
        result.append(True)
    else:
        result.append(False)

print(all(i == True for i in result))
