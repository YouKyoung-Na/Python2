C,K,P =map(int, input().split())  
result = 0
for i in range(1, C+1):
    result += (K*i) + (P*i*i)
print(result)