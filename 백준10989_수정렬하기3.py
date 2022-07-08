# n= int(input())
# nums = []
# for i in range(n):
#     x = int(input())
#     nums.append(x)
# nums.sort()

# for i in nums:
#     print(i)


'''### 메모리 효율적 할당'''
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)