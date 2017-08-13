from itertools import permutations
key, value = input().split()
result = list(permutations([x for x in sorted(key)], int(value)))
for tuples in result:
    print(''.join([x for x in tuples]))
