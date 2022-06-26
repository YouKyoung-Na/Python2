n= int(input())
nums = []
for i in range(n):
    x = int(input())
    nums.append(x)
nums.sort()

for i in nums:
    print(i)