n = input()
l1 = set(map(int, input().split()))
m = input()
l2 = set(map(int, input().split()))
l = l1.union(l2)
print(len(l))
