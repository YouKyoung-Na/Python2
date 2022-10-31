#7. 키와 표준 몸무게
###list 생성
height = []
weight = []

###리스트에 원소 추가
for i in range(150,181,3):  
    height.append(i)   #height 원소 추가

for i in range(len(height)):  
    a = (height[i]-100)*0.9  #a 변수에 계산값 저장
    weight.append(a)  #Weight 원소 추가

### 출력
for i in range(len(height)):
    print(f'{i+1:3d}   {height[i]}cm   {weight[i]:.1f}kg')