# hw 5. 
### 랜덤 모듈 작성
import random

### 변수 선언(점수)
score = 100
cnt = 0

### While 문을 사용해 점수 부여
while(True):  #True 첫 글자 대문자로
    user = int(input('방 번호를 입력하세요: '))
    criminal = random.randint(1,3)  #범인은 다른 방으로 이동하기 때문에 while문 안에 작성 ,범인의 난수 1~3번에서 움직인다. 

    if(user>3):  #3 초과 값을 제시했을 때(존재하지 않는 방)
        cnt +=1  #가독성을 위해서 좀 더 추가했습니다.
        print("------------")   #가독성을 위해서 좀 더 추가했습니다.
        print(cnt, "번 째 시도")
        print(user, "번 방은 없습니다.")
        print("------------")  #가독성을 위해서 좀 더 추가했습니다.
        

    elif(user == criminal):  #범인을 잡았을 때
        cnt +=1  
        print("------------")  
        print(cnt, "번 째 시도")
        print("범인 체포!")
        print("게임 종료")
        print("------------")  
        break
        

    else:  #범인을 놓쳤을 때
        cnt +=1
        print("------------")   
        print(cnt, "번 째 시도")
        score -= 10  #범인을 놓치면 10점씩 감점이 된다.
        print("범인이 없습니다.")
        print("------------")
        continue

### 점수 출력
print("점수: ", score)