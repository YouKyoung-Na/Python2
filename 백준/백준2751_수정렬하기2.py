n = int(input())
nums=[]
for i in range(n):
    a = int(input())
    nums.append(a)
nums.sort()
for i in range(n):
    print(nums[i])
