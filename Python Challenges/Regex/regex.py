import re

t = int(input())
for _ in range(t):
    n = input()
    print(bool(re.match(r"(^[+-]?[0-9]*\.[0-9]+$)", n)))
