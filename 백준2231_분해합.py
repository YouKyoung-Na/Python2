n = int(input())

for i in range(1, n+1):
    if sum(map(int, str(i)))+i == n:  #자릿수마다 더하기
        print(i)
        break  #구해졌으면 멈추기
    if i==n:  #생성자 없는 경우!!!!
        print(0)