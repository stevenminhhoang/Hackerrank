from collections import deque

testcase = int(input())
for _ in range(testcase):
    n = int(input())
    d = deque(map(int, input().split()))
    ls = []
    for _ in range(len(d)):
        a = d.popleft()
        ls.append(a)
        d.reverse()
    # print(ls)
    if all([ls[i] >= ls[i + 1] for i in range(len(ls) - 1)]):
        print('Yes')
    else:
        print('No')
