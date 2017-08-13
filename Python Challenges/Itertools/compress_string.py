from itertools import *
s = input()
for x in [(len(list(items)), int(group)) for group,items in groupby(s)]:
    print(x,end=' ')
