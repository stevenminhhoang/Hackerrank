N, X = map(int, input().split())
ls = list()
for _ in range(X):
    ls.append(list(map(float, input().split())))

for i in zip(*ls):
    print(sum(i) / X)
