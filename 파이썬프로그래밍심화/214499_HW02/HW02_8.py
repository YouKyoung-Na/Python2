# hw8. 과제 3
### math 라이브러리 사용
import math

### a,b,c 값 입력
a,b,c = map(int, input('a,b,c를 공백으로 구분해 입력하세요: ').split())

### 판별식 계산 및 출력
d = (b*b)-4*a*c
if(d>0): # 판별식이 0보다 클 경우
    x1 = ((-b)+(math.sqrt(d)))/(2*a)
    x2 = ((-b)-(math.sqrt(d)))/(2*a)
    print("해가 2개 입니다.")
    print(f'해1: {x1:.2f}, 해2: {x2:.2f}')
elif(d==0):  #판별식이 0일 경우
    x1 = ((-b)+(math.sqrt(d)))/(2*a)
    print("해가 1개 입니다.")
    print(f'해1: {x1:.2f}')
elif(d<0):  #판별식이 0보다 작을 경우
    print("해가 없습니다.")