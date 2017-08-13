def merge_the_tools(string, k):
    l = list(string[i:i + k] for i in range(0, len(string), k))
    for i in l:
        # print([i[x] for x in range(len(i)) if x != x ])
        ls = []
        for x in range(len(i)):
            if any(i[x] == element for element in ls):
                continue
            else:
                ls.append(i[x])
        print("".join(ls))

# merge_the_tools("AABCAAADA", 3)
