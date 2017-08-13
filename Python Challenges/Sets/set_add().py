def stamp():
    stamp = set()
    n = int(input())
    for _ in range(n):
        stamp.add(input())
    print(len(stamp))

stamp()
