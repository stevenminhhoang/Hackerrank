arr = []
for i in range(int(input())):
    s = input().split()
    for i in range(1,len(s)):
        s[i] = int(s[i])
        # print(s[i])

    if s[0] == "insert":
        arr.insert(s[1], s[2])
    if s[0] == "print":
        print(arr)
    if s[0] == "remove":
        arr.remove(s[1])
    if s[0] == "append":
        arr.append(s[1])
    if s[0] == "sort":
        arr.sort()
    if s[0] == "pop":
        arr.pop()
    if s[0] == "reverse":
        arr.reverse()
