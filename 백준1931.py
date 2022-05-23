n=int(input())
time =[]

for i in range(n):
    start, end = map(int, input().split())  #start , end split을 이용해 따로 입력 가능
    time.append([start, end])

time = sorted(time, key = lambda x: x[0]) #start 기준 오름차순 후 end 기준으로 오름차순
time = sorted(time, key = lambda x: x[1])

last = 0 #회의의 마지막 시간을 저장
cnt = 0 #회의 개수를 저장

for i, j in time:
    if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같은경우(시작시간 회의시간 같아도 카운트)
        cnt += 1
        last = j  #time 리스트 안의 회의 마지막 시간을 last에 대입

print(cnt)

