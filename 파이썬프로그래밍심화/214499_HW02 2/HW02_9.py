# hw 09. 과제 4. 구구단 퀴즈

### random, time 라이브러리 사용
import time  #time library
import random #random library

#점수 변수 저장
score = 100
### 5번 동안 반복
for i in range(5):
    n = random.randint(1,9)
    m = random.randint(1,9)

    # random하게 n, m 만들어 n x m으로 저장하기
    result = n*m

    # Time Start!
    startTime = time.time()  #시작시간 설정하기

    # 사용자 값 입력 받기
    human = int(input(f'문제[{i+1}] {n} x {m} = '))
    #끝시간 설정하기
    endTime = time.time()  

    # 시간 종료후 총 시간 계산
    realTime = endTime - startTime  #시간 계산하기

    # n x m의 결과와 사용자가 입력한 결과 비교하기
    if(result == human):
        if(realTime <= 2):  # 정답 맞췄는지 여부 판단(시간내에 맞췄는가? 답을 맞췄는데 초과했는가? 틀렸는가?)
            print("시간 내에 맞췄어요!")
        elif(realTime > 2):
            print("답은 맞췄는데, 시간이 초과되었습니다. ㅠ_ㅠ")
            score -= 20  # 시간 초과되었을 경우 -20
    elif(result != human):
        print("땡 틀렸습니다!")
        score -= 20  # 틀렸을 경우 -20

### 총 점수 계산(총점 100점)
print(f'당신의 점수는 {score} 입니다.')