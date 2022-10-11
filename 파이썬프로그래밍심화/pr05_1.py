# 1. 
### 변수 선언
nums = []
result = 0

### 입력, for 문을 이용해 처리
for i in range(1, 5):
    num  = int(input(f'{i}번째 숫자: '))
    nums.append(num)

for i in nums:
    result +=i 

### 출력
print('합계 ==> ', result)