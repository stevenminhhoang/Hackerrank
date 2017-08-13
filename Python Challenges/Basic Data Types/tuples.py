n = int(input())
input_list = input().split()
input_list = [int(x) for x in input_list]
# print(input_list)
t = tuple(input_list)
print(hash(t))
