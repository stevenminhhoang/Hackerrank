import re

s = input()
for i in re.split(r'[,.]',s):
    if i.isdigit():
        print(i)
