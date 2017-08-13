n , m = input(), input().split()
print(all([int(x) > 0 for x in m]) and any([int(x) == int(x[::-1]) for x in m]))
