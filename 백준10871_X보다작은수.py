n, x = map(int, input().split())
nums = list(map(int, input().split()))
list1 = []
for i in range(n):
    if(nums[i]<x):
        list1.append(nums[i])

print(" ".join(map(str,list1)))