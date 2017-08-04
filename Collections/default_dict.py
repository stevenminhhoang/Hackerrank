from collections import defaultdict

n, m = list(map(int, input().split()))
a = list()
b = list()
for _ in range(n):
    a.append(input())
for _ in range(m):
    b.append(input())

for element in b:
    if element in a:
        indices = [str(i + 1) for i, x in enumerate(a) if x == element]
        print(' '.join(indices))
    else:
        print(-1)



# a = ["ok", "bar", "foo", "bar"]
# indices = [str(i) for i, x in enumerate(a) if x == "bar" ]
# print(' '.join(indices))
