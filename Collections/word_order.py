from collections import OrderedDict

n = int(input())
ls = []
D = OrderedDict()

for _ in range(n):
    i = input()
    ls.append(i)
    D[i] = D.get(i, 0) + 1

print(len(D))
print(' '.join(map(str, D.values())))
