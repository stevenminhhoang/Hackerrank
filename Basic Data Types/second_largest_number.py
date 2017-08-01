n = int(input())
arr = list(map(int, input().split()))
sortedArray = sorted(set(arr))
secondLarget = sortedArray[-2]
print(secondLarget)
