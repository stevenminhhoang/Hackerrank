def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return "".join(l)

# print(mutate_string("Hoang", 0, "L"))
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)
