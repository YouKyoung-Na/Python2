# hw3.
### 변수선언
num =0

### 입력(시작값, 끝값, 증가값)
start = int(input('시작값을 입력하세요 : '))
stop = int(input('끝값을 입력하세요 : '))
step = int(input('증가값을 입력하세요: '))

### for문을 이용해 처리
for i in range(start, stop+1, step):   #stop index도 포함하기 위해 stop+1로 처리. 
    num +=i

### 출력
print(start, '에서', stop, '까지', step, '씩 증가시킨 값의 합계 : ', num)