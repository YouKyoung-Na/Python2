# 5번

### 입력
#### 합계
f_hundred = int(input('500원짜리 개수: '))  #동전 개수 입력
o_hundred = int(input('100원짜리 개수: '))
fifty = int(input('50원짜리 개수: '))
ten = int(input('10원짜리 개수: '))

### 동전 합계 계산 및 출력
sum = (f_hundred*500)+(o_hundred*100)+(fifty*50)+(ten*10)
print(f'@@ 동전의 합계 ==> {sum}')

#### 교환
n = int(input('교환할 돈: '))


####출력
remain1 = int(n/500)  #타입 int형으로 캐스팅
print(f'500원짜리 개수 ==> {remain1}')  # 몫 출력

remain2 = int(n-(remain1*500))//100  # 남은돈 계산
print(f'100원짜리 개수 ==> {remain2}')

remain3 = int(n-((remain1*500)+(remain2*100)))//50
print(f'50원짜리 개수 ==> {remain3} ')

remain4 = int(n-((remain1*500)+(remain2*100)+(remain3*50)))//10
print(f'10원짜리 개수 ==> {remain4}')

remain5 = int(n-((remain1*500)+(remain2*100)+(remain3*50)+(remain4*10)))
print(f'@@ 잔돈 ==> {remain5}')