#1.
### 변수 선언
list1 = []  #리스트 선언
sum1 = 0  # 합계 변수 선언

### 입력(시작값, 끝값, 증가값)
for i in range(10,41,10):  #10~40번째 인덱스까지 10씩 증가
    list1.append(i)  #리스트에 원소 추가

### for문을 이용해 처리
for i in list1:
    sum1 +=i  #합계에 더함

### 출력
for i in range(len(list1)):
    print(f'{i+1}번째 숫자: {list1[i]}')  #list 원소 출력

print('합계==>',sum1)  #합계 출력