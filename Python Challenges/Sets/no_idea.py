def no_idea(arr, a, b):
    happiness = 0
    for i in arr:
        if i in a:
            happiness += 1
        if i in b:
            happiness -= 1
    print(happiness)

# m,n = list(map(int, input().split()))
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

no_idea(arr, a, b)
