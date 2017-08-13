from itertools import *
K, M = list(map(int, input().split()))
array = list([map(int, input().split()[1:]) for _ in range(K)])
def f(arr):
    return sum(x ** 2 for x in arr) % M

print(max(list(map(f, list(product(*array))))))
