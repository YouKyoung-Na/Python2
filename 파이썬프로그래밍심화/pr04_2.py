# 2. 다이아몬드 출력하기
### 입력
num = int(input('별 최대 개수 : '))

### 다이아몬드 만들기 위한 반복문 처리 및 출력
if(num%2 !=0):  #입력값이 홀수일 때
    i = 1
else:  #입력값이 짝수일 때
    i = 2

for i in range(i, num+1 ,2):  #다이아몬드 위 쪽
    blank = ' '*((num-i)//2)  ##num에서 i를 빼고 2로 나눈 후 양 옆으로 공백을 준다. 
    print(blank, '*'*i, blank)

for i in range(i-2, 0, -2):  #다이아 몬드 아래쪽
    blank = ' '*((num-i)//2)  
    print(blank, '*'*i, blank)