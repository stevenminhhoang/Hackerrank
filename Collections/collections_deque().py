from collections import deque

d = deque()
n = int(input())
for _ in range (n):
    argv = input().split()
    if argv[0] == 'append':
        d.append(argv[1])
    elif argv[0] == 'appendleft':
        d.appendleft(argv[1])
    elif argv[0] == 'pop':
        d.pop()
    elif argv[0] == 'popleft':
        d.popleft()

print(' '.join(d))
