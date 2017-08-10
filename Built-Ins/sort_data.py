n, m = map(int, input().split())
ls = []
for _ in range(n):
    ls.append(list(map(int, input().split())))

k = int(input())
sort_data = sorted(ls, key = lambda x: x[k])
for i in sort_data:
    print(' '.join([str(x) for x in i]))
