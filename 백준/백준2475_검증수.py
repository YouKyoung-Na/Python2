n=list(map(int,input().split()))
result=0
for i in n:
    result += pow(i,2)
print(result%10)