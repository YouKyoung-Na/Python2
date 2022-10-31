#2. 
#numpy 간절하게 쓰고싶습니다...
### 입력
n = int(input('N을 입력하세요: '))
ls = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19]]  #4행 5열 2차원 배열 선언 
result = [[n]*5]*4  #n으로 구성된 행령 생성

### 처리 및 출력
for i in range(len(ls)):  #행렬의 곱
    result[i] = [a*b for a,b in zip(ls[i], result[i])]  #list comprehension 사용

for i in result:  #출력 코드
    for j in i:
        print(f'{j:3d}', end='') #공백 생성
    print()