'''
def hansu(n):
    cnt = 0
    for i in range(1, n+1):  
        num_list = list(map(int, str(i)))
        if i < 100 :
            cnt += 1
        elif num_list[1]-num_list[0] == num_list[2]-num_list[1]:
            cnt +=1
    return cnt

n= int(input())
print(hansu(n))
'''

n, k= map(int, input().split())
coin_list =[]
cnt =0
for i in range(n):
    coin_list.append(int(input()))

for i in reversed(range(n)):
    cnt += k // coin_list[i]
    k %= coin_list[i]
print(cnt)