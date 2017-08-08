from collections import OrderedDict
s = list(input())
sorted_string = sorted(s)
D = OrderedDict()
for i in sorted_string:
    D[i] = D.get(i, 0) + 1

sorted_dict = sorted(D.items(), key = lambda x: x[1], reverse = True)[:3]
for i, j in sorted_dict:
    print(i, j)
