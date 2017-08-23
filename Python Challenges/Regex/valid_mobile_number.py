import re


for _ in range(int(input())):
    m = re.match(r'^[789]\d{9}$', input())
    if bool(m) == True:
        print('YES')
    if bool(m) == False:
        print('NO')
