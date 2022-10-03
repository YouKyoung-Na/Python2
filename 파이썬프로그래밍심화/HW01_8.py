###math 라이브러리 설치 및 사용
import math

###임의의 두 점 사이의 거리 계산
#임의의 두 점 입력
x1, y1 = map(int,input('임의의 점1(x1, y1)을 입력하시오: ').split())  #두 점을 공백으로 구분, 입력
x2, y2 = map(int,input('임의의 점2(x2, y2) 를 입력하시오: ').split())

#거리 계산
dis1 = math.sqrt(((x1-x2)**2)+((y1-y2)**2))  #거리 공식 활용

#출력
print(f'두 점 사이의 거리 ==> {dis1:.2f}')  #소수점 둘째 자리까지 입력

### 임의의 한 점과 직선 사이의 거리 계산
# 임의의 한 점과 직선 정보 입력
x3, y3 = map(int,input('임의의 한 점(x3, y3)을 입력하시오: ').split())  #두 점을 공백으로 구분 및 입력
a, b = map(int,input('y = ax+b 의 a, b를 입력하시오: ').split())

# 거리 계산
dis2 = (abs((a*x3)-y3+b))/(math.sqrt((a**2) + (b**2)))   #y=ax+b를 일반형으로 풀면 ax-y+b=0

# 출력
print(f'임의의 한 점과 직선 사이의 거리 ==> {dis2:.2f}')  #소수점 둘째자리까지 입력