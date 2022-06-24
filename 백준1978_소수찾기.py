import math
def isPrime(num):
    if num ==1 : return False

    sq = int(math.sqrt(num))

    for i in range(2,sq+1):
        if num%i == 0: return False
    return True

n = int(input())
x = map(int, input().split())
cnt = 0
for i in x:
    if isPrime(i):
        cnt+=1
print(cnt)