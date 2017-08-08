import re

n = int(input())

for _ in range(n):
    try:
        boolean = True
        pattern = input()
        re.compile(pattern)
    except re.error:
        boolean = False

    print(boolean)
