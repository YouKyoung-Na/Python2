n = int(input())
cnt = 1
a = 1  #벌집의 개수

while n > a :
    a += 6*cnt
    cnt +=1
print(cnt)