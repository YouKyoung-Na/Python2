n=int(input())
a=[]
for i in range(1,n+1):
    a.append(i)
a.sort(reverse=True)

for i in a:
    print(i)

# 정석
# n = int(input())
# for i in range(n, 0, -1):
#     print(i)