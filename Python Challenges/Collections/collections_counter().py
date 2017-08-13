from collections import *

total = 0
x = int(input())
X = Counter(list(map(int, input().split())))
n = int(input())

for _ in range(n):
    size, price = list(map(int, input().split()))
    if X[size]:
        total += price
        X[size] -= 1

print(total)
