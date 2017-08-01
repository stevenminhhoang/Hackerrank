def swap_case(s):
    new_string = []
    for char in s:
        if char.islower():
            char = char.upper()
            new_string.append(char)
        elif char.isupper():
            char = char.lower()
            new_string.append(char)
        else:
            new_string.append(char)

    return "".join(new_string)

s = input()
result = swap_case(s)
print(result)
