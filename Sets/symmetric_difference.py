def symmetric_difference(a, b):
    ls = sorted(a.symmetric_difference(b))
    for x in ls:
        print(x)


m = int(input())
mlist = set(map(int, input().split()))
n = int(input())
nlist = set(map(int, input().split()))
symmetric_difference(mlist, nlist)
