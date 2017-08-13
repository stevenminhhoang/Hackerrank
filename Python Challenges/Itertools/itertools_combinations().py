from itertools import combinations
key, value = input().split()
for i in range(1, int(value) + 1):
    result = list(combinations([x for x in sorted(key)], i))
    for tuples in result:
        print(''.join([x for x in tuples]))
