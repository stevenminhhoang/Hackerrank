i = input()
a = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    argv = input().split()
    b = set(map(int, input().split()))
    if argv[0] == 'intersection_update':
        a.intersection_update(b)
    if argv[0] == 'update':
        a.update(b)
    if argv[0] == 'symmetric_difference_update':
        a.symmetric_difference_update(b)
    if argv[0] == 'difference_update':
        a.difference_update(b)
        
print(sum(a))
