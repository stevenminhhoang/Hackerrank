s = input()
sorted_string = sorted(s, key = lambda x: (x.isdigit() and int(x) % 2 == 0, x.isdigit(), x.isupper(), x.islower(), x))
print(*sorted_string, sep='')
