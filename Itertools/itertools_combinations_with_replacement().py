from itertools import combinations_with_replacement
key, value = input().split()
result = list(combinations_with_replacement([x for x in sorted(key)], int(value)))
for tuples in result:
    print(''.join([x for x in tuples]))
