from itertools import *
length = int(input())
n = input().split()
k = int(input())
result = list(combinations(n, k))
f = list(filter(lambda res: 'a' in res, result))
print(len(f) / len(result))
